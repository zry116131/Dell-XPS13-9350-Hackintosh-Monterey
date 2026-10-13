# 发布校验记录

发布日期：2026-10-13。

- OpenCore 1.0.9 ocvalidate：通过。
- 所有 plist 可解析，启用的驱动、ACPI、kext 文件引用存在。
- 相对最后恢复的 U 盘基线，config.plist 仅替换四项私人身份字段：SystemSerialNumber、MLB、SystemUUID、ROM。
- 保留的 EFI 二进制、ACPI、USB 映射与本地基线逐字节一致；移除未启用主题资源和 Finder 元数据。
- 对已知私人身份、局域网信息、账号路径、SSH 标记及令牌模式扫描，无匹配。
- 原始日志、恢复镜像、照片、密钥、sudo 配置不在发布目录。
- 静态校验不等于启动验收。脱敏模板需自行填写身份，最后实机验证仍以 README 记录为准。
