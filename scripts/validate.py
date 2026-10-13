#!/usr/bin/env python3
"""Check package references and SMBIOS fields; does not prove hardware compatibility."""
import argparse
import plistlib
import uuid
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--require-identity', action='store_true')
args = parser.parse_args()
root = Path(__file__).resolve().parent.parent
oc = root / 'EFI/OC'
c = plistlib.loads((oc / 'config.plist').read_bytes())
errors = []

def require(path):
    if not path.is_file():
        errors.append('Missing: ' + str(path.relative_to(root)))

require(root / 'EFI/BOOT/BOOTx64.efi')
require(oc / 'OpenCore.efi')
for entry in c['ACPI']['Add']:
    if entry['Enabled']:
        require(oc / 'ACPI' / entry['Path'])
for entry in c['UEFI']['Drivers']:
    if entry['Enabled']:
        require(oc / 'Drivers' / entry['Path'])
for entry in c['Kernel']['Add']:
    if entry['Enabled']:
        bundle = oc / 'Kexts' / entry['BundlePath']
        require(bundle / entry['PlistPath'])
        if entry['ExecutablePath']:
            require(bundle / entry['ExecutablePath'])
for file in (root / 'EFI').rglob('*.plist'):
    plistlib.loads(file.read_bytes())
g = c['PlatformInfo']['Generic']
if args.require_identity:
    for key in ('SystemSerialNumber', 'MLB', 'SystemUUID'):
        if not g.get(key):
            errors.append('Fill PlatformInfo/Generic/' + key)
    try:
        if uuid.UUID(g['SystemUUID']).int == 0:
            raise ValueError()
    except (ValueError, AttributeError):
        errors.append('SystemUUID must be a nonzero UUID')
    if not isinstance(g.get('ROM'), bytes) or len(g['ROM']) != 6 or g['ROM'] == bytes(6):
        errors.append('ROM must contain six nonzero-identity bytes (Data)')
else:
    if any(g[k] for k in ('SystemSerialNumber', 'MLB', 'SystemUUID')) or g['ROM'] != bytes(6):
        errors.append('Public package unexpectedly contains SMBIOS identity values')
if errors:
    raise SystemExit('\n'.join(errors))
print('PASS: plist parsing, enabled file references, identity-field checks.')
if not args.require_identity:
    print('Public template: fill your own identity before deployment.')
print('Also run ocvalidate from OpenCore 1.0.9; bootability still requires testing.')
