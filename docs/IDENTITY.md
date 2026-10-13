# 填写自己的设备身份

编辑 `EFI/OC/config.plist` 中 `PlatformInfo/Generic`：

| 字段 | 发布包内容 | 应填写内容 |
|---|---|---|
| SystemProductName | MacBookPro13,1 | 保持该模型作为本配置基线 |
| SystemSerialNumber | 空字符串 | 自己生成的对应模型序列号 |
| MLB | 空字符串 | 同组生成的主板序列号 |
| SystemUUID | 空字符串 | 自己生成的有效 UUID |
| ROM | 6 字节全零 Data | 自己机器使用的 6 字节值，保持 Data 类型 |

用 plist 编辑器或 GenSMBIOS 填写，避免把 ROM 错填成普通字符串。不要把生成后的私人配置重新提交到公共仓库。

`python3 scripts/validate.py --require-identity` 只检查结构和非空条件，不判断 Apple 服务可用性，也不验证身份的唯一性。身份准备后还需用 OpenCore 1.0.9 的 ocvalidate 检查。
