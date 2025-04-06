graph TD
    A["MA-BLSTM模型训练诊断综合视图"] --> B["(a) 训练动态监控"]
    A --> C["(b) 混淆矩阵"]
    A --> D["(c) 故障检出率"]

    B --> B1["双Y轴布局"]
    B1 --> B1a["左轴: 交叉熵损失曲线\n（指数移动平均）"]
    B1 --> B1b["右轴: 准确率曲线\n（训练/测试集）"]
    B1b --> B1b1["星形标记最佳测试点\n(epoch 45, 98.2%)"]
    B1 --> B1c["余弦退火学习率曲线\n(T_0=10周期)"]

    C --> C1["归一化混淆矩阵"]
    C1 --> C1a["对角线强化显示\n(深蓝: 高正确率)"]
    C1 --> C1b["红框标注决策边界\n(95%置信区间)"]
    C1 --> C1c["t-SNE特征分布子图\n(右下角嵌入)"]

    D --> D1["横向柱状图"]
    D1 --> D1a["颜色阈值区分\n(绿色>90%, 红色<90%)"]
    D1 --> D1b["紫色虚线标注\n平均检出率(92.6%)"]
    D1 --> D1c["显著性标记\n(类别15异常值)"]

    style A fill:#f0f8ff,stroke:#333,stroke-width:2px
    style B fill:#e6f3ff,stroke:#1a8cff
    style C fill:#e6f3ff,stroke:#1a8cff
    style D fill:#e6f3ff,stroke:#1a8cff
    classDef subgraph fill:#ffffff,stroke:#1a8cff,stroke-width:1px;
    class B1,B1a,B1b,B1c,C1,C1a,C1b,C1c,D1,D1a,D1b,D1c subgraph;
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5NDU5MzMyMTVdfQ==
-->