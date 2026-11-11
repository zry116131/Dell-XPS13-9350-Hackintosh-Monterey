# Third-party components

This repository packages a machine-specific configuration with upstream bootloader and driver binaries. No blanket license is asserted over third-party components. Original copyright notices remain applicable. The notices in `licenses/` are upstream license texts retrieved during packaging; consult each upstream repository for complete source and current notices.

| Component | Source |
|---|---|
| OpenCore / OpenRuntime / ResetNvramEntry | https://github.com/acidanthera/OpenCorePkg |
| Lilu | https://github.com/acidanthera/Lilu |
| WhateverGreen | https://github.com/acidanthera/WhateverGreen |
| AppleALC | https://github.com/acidanthera/AppleALC |
| VirtualSMC and SMC plugins | https://github.com/acidanthera/VirtualSMC |
| AirportBrcmFixup | https://github.com/acidanthera/AirportBrcmFixup |
| BrcmFirmwareData / BrcmPatchRAM3 / BlueToolFixup | https://github.com/acidanthera/BrcmPatchRAM |
| NVMeFix | https://github.com/acidanthera/NVMeFix |
| BrightnessKeys | https://github.com/acidanthera/BrightnessKeys |
| VoodooPS2Controller / VoodooInput | https://github.com/acidanthera/VoodooPS2 |
| VoodooI2C / VoodooI2CHID | https://github.com/VoodooI2C/VoodooI2C |
| USBToolBox | https://github.com/USBToolBox/kext |
| Sinetek-rtsx | https://github.com/cholonam/Sinetek-rtsx |
| HfsPlus | https://github.com/acidanthera/OcBinaryData |
| Initial ACPI/config generation | https://github.com/lzhoang2801/OpCore-Simplify |

`docs/components.json` records installed bundle version labels. Binary hashes are recorded in `SHA256SUMS.txt`; labels alone do not establish a reproducible source build. The local USB map was edited for this machine. Generated ACPI tables are hardware-specific configuration artifacts.

USBToolBox source includes “Copyright © 2020-2021 Dhinak G. All rights reserved.” Sinetek-rtsx contains work from multiple contributors and OpenBSD-derived code with per-file notices. HfsPlus is distributed by OcBinaryData as a binary. These projects do not expose a single root license file in the inspected trees; this package does not relicense them or assert additional redistribution rights.


## Sequoia additions (2026-11-11)

The `Sequoia/` integration follows https://github.com/Edwardwich/BCM-WIFI-Sequoia at commit `d443a5e8741581446142d844100370ea3ff74199`. Additional components include AMFIPass (binary supplied by the above integration), RestrictEvents (https://github.com/acidanthera/RestrictEvents), and the ECM-Override codeless configuration from the machine's working EFI. IOSkywalkFamily and IO80211FamilyLegacy/AirPortBrcmNIC contain Apple-origin components retained from that working integration; they are not relicensed as open-source code by this repository. Original notices remain in their bundles. Component labels and file hashes do not establish a reproducible build or grant additional rights.

OCLP 2.4.1 (https://github.com/dortania/OpenCore-Legacy-Patcher) was used for system-volume patches on the test machine. The patched system frameworks and macOS installer are not included. Sequoia component labels are in `Sequoia/components.json`; hashes are in `Sequoia/SHA256SUMS.txt`.
