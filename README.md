<p align="center">
  <a href="https://orcastor.github.io/doc/">
    <img src="https://orcastor.github.io/doc/logo.svg">
  </a>
</p>

<p align="center"><strong>📱OrcaS 常见手机照片</strong></p>

### 照片名称列表

- [android](android/android)
- [ios](ios/ios)
- （可能用不上，安卓可以用数据库查询，iOS直接拼出名字）

### 使用场景

- 可以使用厂商和型号匹配到对应的机型图片
- Android：sqlite数据库[android.db](android.db)
  - 表名models，字段名model，有FTS5版全文检索索引（注意是否支持，如不支持可修改[models2db.py](models2db.py)自行生成）
  - 建议查询方式
    - `SELECT * FROM models WHERE model LIKE ? COLLATE NOCASE`
    - 查询参数：`%<ro.product.brand>%<ro.product.name>%`，比如`%Huawei%NOP-AN00P%`
        ``` cmd
        PS F:\GitHub\phone_images> sqlite3.exe .\android.db
        SQLite version 3.45.2 2024-03-12 11:06:23 (UTF-16 console I/O)
        Enter ".help" for usage hints.
        sqlite> SELECT * FROM models WHERE model LIKE '%Huawei%NOP-AN00P%' COLLATE NOCASE;
        Huawei Mate 40 RS Porsche Design NOP-AN00P Black
        Huawei Mate 40 RS Porsche Design NOP-AN00P
        sqlite>
        ```
- iOS：[model_to_color.json](model_to_color.json)映射表
  - 可以使用M或者N开头的5位型号（`ModelNumber`）匹配到颜色
      - 参考资料一：[iPhone 15型号表](https://ek.ua/en/post/5188/122-how-not-to-make-a-mistake-iphone-article-numbers-and-their-decoding/)
      - 参考资料二：[iPhone 15以前型号表](https://github.com/pbakondy/ios-device-list/blob/b50e6818ae5d24c80bef0594a4c43da58f58ceb1/iphone.json)
      - 参考资料三：[苹果设备Model信息](https://www.theiphonewiki.com/wiki/Models)
  - 规约到12种颜色
      - Black：Black、Midnight、Graphite、Jet Black、Matte Black、BlackSlate、Black Titanium
      - White：White、Starlight、WhiteSilver、White Titanium
      - Gold：Gold
      - Silver：Silver
      - Pink: Pink、Rose Gold
      - Gray：Gray、Space Gray、Natural Titanium
      - Blue：Blue、Sierra Blue、Pacific Blue、Blue Titanium
      - Red：Red
      - Green：Green、Alpine Green
      - Yellow：Yellow
      - Purple: Purple、Deep Purple
      - Orange：Coral

#### Golang SDK

- 提供`GetIOSProductName`,`GetIOSURL`,`GetAndroidProductName`,`GetAndroidURL`四个方法
- 引入方式`import "github.com/orcastor/phone_images/sdk"`

### 构造地址

- 推荐CDN地址：https://raw.githubusercontent.com/orcastor/phone_images/master/[platform]/[name].jpg
- ~~不推荐跳转地址: https://github.com/orcastor/phone_images/blob/master/[platform]/[name].jpg?raw=true~~
- **\* 空格需要替换为`%20`**

### 示例

- Huawei Mate 40 RS

  - 地址为：https://raw.githubusercontent.com/orcastor/phone_images/master/android/Huawei%20Mate%2040%20RS%20Porsche%20Design%20NOP-AN00P.jpg

    <img src="https://raw.githubusercontent.com/orcastor/phone_images/master/android/Huawei%20Mate%2040%20RS%20Porsche%20Design%20NOP-AN00P.jpg" width="30%">

- iPhone 15 Black

  - 地址为：https://raw.githubusercontent.com/orcastor/phone_images/master/ios/iPhone%2015%20Black.jpg

    <img src="https://raw.githubusercontent.com/orcastor/phone_images/master/ios/iPhone%2015%20Black.jpg" width="30%">