# 本机配置说明

## HD 520 / QHD+ 内屏

路径 `PciRoot(0x0)/Pci(0x2,0x0)`：

| 属性 | Data 十六进制 |
|---|---|
| AAPL,ig-platform-id | 00001619 |
| framebuffer-patch-enable | 01000000 |
| framebuffer-stolenmem | 00008001 |
| framebuffer-fbmem | 00004000 |

分别为 24 MiB stolen memory、4 MiB framebuffer memory 的配置。在这台 3K 屏机器上验证了 Metal 和内屏显示；不要把它直接套用到不同核显/屏幕。

## DW1820A 无线

硬件 PCI 14e4:43a3，子系统 1028:0023。路径 `PciRoot(0x0)/Pci(0x1c,0x4)/Pci(0x0,0x0)`：

- `compatible`：字符串 `pci14e4,43a0`
- `pci-aspm-default`：Data `00000000`
- boot-args：`brcmfx-aspm=0 brcmfx-delay=15000`
- AirportBrcmFixup 2.2.1 父驱动；不加载其 AirPortBrcm4360/AirPortBrcmNIC 注入插件。

## 蓝牙和 USB

- 蓝牙 USB ID：0a5c:6412。
- UTBMap 新增 `HSBT`：物理端口编号 3，`UsbConnector=255`（内部）。映射的端口名称不一定等于物理编号，请以 `port` Data 为准。
- 其余保留物理端口 1、2、4、5、13、14；这是该机采集的局部映射，不是全机型模板。
- BrcmFirmwareData + BrcmPatchRAM3 + BlueToolFixup 2.7.1；Monterey 不搭配旧 BrcmBluetoothInjector。

## 保留的设置

- SMBIOS 模型 MacBookPro13,1（私人身份需自行填写）。
- 原始 ACPI、电源管理和输入驱动保持不变。
- `-vi2c-force-polling` 保留；不要把它误当作 `-v` 删除。
- `LauncherOption=Disabled`，避免持续自动创建固件启动入口；已有重复入口需在 BIOS 中根据实际路径处理。
- `HibernateMode=None`，不含 HibernationFixup。

参考：[WhateverGreen](https://github.com/acidanthera/WhateverGreen)、[AirportBrcmFixup](https://github.com/acidanthera/AirportBrcmFixup)、[BrcmPatchRAM](https://github.com/acidanthera/BrcmPatchRAM)、[USBToolBox](https://github.com/USBToolBox/kext)。
