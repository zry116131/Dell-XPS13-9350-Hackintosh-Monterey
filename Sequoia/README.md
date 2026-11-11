# XPS 9350 · Sequoia 15.8.2（24H232）

2026-11-11 实机基线：i5-6200U / 8GB / HD 520 / 3200×1800 / DW1820A。OpenCore 1.0.9，SMBIOS **MacBookPro15,2**。

## 已验证

- Lilu 1.7.2 RELEASE + AirportBrcmFixup 2.1.9 RELEASE 已通过加载 UUID 核对。
- Wi-Fi 自动关联、无线 SSH、绑定无线接口 HTTPS 200、5MB 下载、关闭再开启后的重连。
- 两次连续 U 盘软重启到登录界面/桌面；写入内置 EFI 后，拔 U 盘软重启，硬盘独立启动和无线联网通过。
- HD 520 报告 Metal 3、1536MB，内屏 3200×1800、看起来像 1600×900。此项是系统识别结果，不表示全部图形工作负载均已验证。

## 使用前提

1. 备份自己的 EFI 和数据，保留独立可启动的恢复 U 盘。
2. 为 **MacBookPro15,2** 生成自己的 SystemSerialNumber、MLB、SystemUUID 和 6 字节 ROM，填入本目录 `EFI/OC/config.plist → PlatformInfo → Generic`。本包上述身份字段为空或零。
3. 仓库根目录执行 `python3 scripts/validate.py --root Sequoia --require-identity`，再使用 OpenCore 1.0.9 的 ocvalidate 检查 `Sequoia/EFI/OC/config.plist`。
4. 只把本目录的 `EFI/` 放到测试启动盘根目录；不要与仓库根目录 Monterey EFI 合并。
5. 本机系统卷使用 **OCLP 2.4.1 Modern Wireless 根补丁**，支持资源版本 1.9.5。已有补丁记录包含 13.7.2-24 无线框架、14.7.2 WiFiAgent。EFI 包不含这些系统卷文件、不含系统安装镜像，单独复制 EFI 无法复现完整系统状态。Hackintosh 并非 OCLP 官方支持目标，不要照搬其自动生成的 Mac EFI。
6. 先验证桌面、输入、无线和重启，再迁入硬盘；不要直接覆盖唯一能启动的配置。系统更新后可能需要重新处理根补丁，应保留恢复方案。

## 无线配置及来源

采用 [Edwardwich/BCM-WIFI-Sequoia](https://github.com/Edwardwich/BCM-WIFI-Sequoia) 方案，参考提交 `d443a5e8741581446142d844100370ea3ff74199`，结合本机 ACPI、USB 映射、输入和蓝牙配置：

- Lilu 1.7.2 RELEASE、AirportBrcmFixup 2.1.9 RELEASE。
- IOSkywalkFamily 1.0、IO80211FamilyLegacy 1200.12.2b1 / AirPortBrcmNIC 1400.1.1、AMFIPass 1.4.1；完整标签见 [components.json](components.json)。
- DW1820A compatible 为 `pci14e4,43a0`，ASPM 属性为 0，`brcmfx-aspm=0 brcmfx-delay=15000`。
- 禁用 BCMWLANCompanion 和 Fixup injector；保留 IOSkywalk 阻止项和已测加载顺序。
- 保留 `-v debug=0x100 keepsyms=1 -vi2c-force-polling -igfxsklaskbl revpatch=sbvmm brcmfx-aspm=0 brcmfx-delay=15000 -liludbgall -brcmfxdbg liludump=90`，未为发布擅自精简参数。核心组件为 RELEASE，仍含诊断参数。
- Lilu 1.7.3 组合曾停在 FakeBrcm、没有无线接口；1.7.2 配套版本恢复交接。尚未证明精确源码根因，勿仅凭版本更新就替换驱动。

## 验证边界及发布处理

无线图标偶尔变空、联网仍正常，原因尚未证实；冷启动、睡眠唤醒、长时间压力、所有外设未完整验证。Monterey 的浅睡结果不可当作 Sequoia 的验收结果，也不要直接运行旧系统浅睡脚本。

来源为已安装、校验的实机 EFI 快照。发布时仅保留启用组件所需目录，排除历史配置、实验备份、日志和元数据；清空 SMBIOS 私有身份，并移除本机蓝牙控制器 NVRAM 缓存。保留的驱动和 ACPI 二进制逐文件与快照一致。脱敏后的配置未在目标机器重新启动，静态校验不等于整机回归。

校验清单为本目录 `SHA256SUMS.txt`（在本目录运行 `shasum -a 256 -c SHA256SUMS.txt`）。第三方组件来源和权利说明见仓库 [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md)。
