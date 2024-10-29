![](https://github.com/syntaxerrortion/SmartTVTool/blob/main/Screenshot_20241029_215955.png)


# SmartTVTool
Smart TV üzerinde bulunan adb portunu kullanarak bu araç ile istediğiniz (.mp4) formatını akıllı TV’nizde oynatabilir ve aynı zamanda kapatabilirsiniz.


### Smart TV Tool Aracı Açıklaması ###


#### Amaç:
Bu araç, yerel ağınızdaki Smart TV'leri veya Android TV cihazlarını tespit etmek ve bu cihazlara belirli komutlar göndermek amacıyla geliştirilmiştir. Özellikle, bu araç, cihazların 5555 numaralı portunun açık olduğunu varsayarak, cihazlara ADB (Android Debug Bridge) üzerinden bağlanmayı hedeflemektedir.


#### Özellikler:
1. **Ağ Taraması**: Yerel ağdaki cihazları tarar ve 5555 numaralı portu açık olan cihazları tespit eder.
2. **Cihaza Bağlanma**: Tespit edilen cihazlara ADB kullanarak bağlanır.
3. **Dosya Yükleme ve Video Oynatma**: Kullanıcının belirttiği bir video dosyasını cihaza yükler ve cihazda bu videoyu oynatır.


### Önemli Noktalar:
- **ADB (Android Debug Bridge)**: Bu araç, ADB kullanarak cihazlara bağlanır ve komutlar gönderir. ADB'nin cihazda ve bilgisayarda doğru şekilde kurulu ve çalışır durumda olduğundan emin olunmalıdır.
- **Nmap**: Ağ taraması için `nmap` kullanılır. `nmap`'in bilgisayarınızda kurulu ve PATH değişkenine ekli olduğundan emin olunmalıdır.
- **Güvenlik**: Bu tür araçlar, yalnızca yasal ve etik amaçlarla kullanılmalıdır. Başkalarının ağlarına ve cihazlarına izinsiz erişim sağlamak yasa dışıdır ve ciddi sonuçlar doğurabilir.

Bu araç, ağınızdaki Smart TV veya Android TV cihazlarına dosya göndermek ve bu cihazlarda video oynatmak gibi işlemleri kolaylaştırır. Ancak, her zaman etik ve yasal sınırlar içinde kalmaya özen gösterilmelidir.
