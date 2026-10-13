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
