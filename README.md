# ChatApp

## Proje Açıklaması

Bu proje, Python'un standart `socket` ve `threading` kütüphaneleri kullanılarak geliştirilmiş, Nesne Tabanlı Programlama (OOP) prensiplerine uygun, çok kullanıcılı (multi-client) bir TCP chat uygulamasıdır.

Uygulama, bir sunucu (server) ve bu sunucuya bağlanabilen birden fazla istemciden (client) oluşur. Sunucu, gelen bağlantıları kabul eder ve bir istemciden aldığı mesajı, o an bağlı olan diğer tüm istemcilere gerçek zamanlı olarak yayınlar (broadcast).

## Temel Özellikler

* **Çok Kullanıcılı:** Sunucu, aynı anda birden fazla istemci bağlantısını yönetebilir.
* **Nesne Tabanlı Tasarım:** Kod, `ChatServer` ve `ChatClient` sınıfları kullanılarak modüler ve yönetilebilir bir yapıda organize edilmiştir.
* **Threading (İş Parçacıkları):**
    * Sunucu tarafında, her istemci bağlantısı ayrı bir thread üzerinde yönetilir.
    * İstemci tarafında, mesaj gönderme ve mesaj alma işlemleri eş zamanlı olarak iki ayrı thread üzerinde çalışır.
* **Gerçek Zamanlı İletişim:** TCP soketleri sayesinde anlık ve kayıpsız veri iletişimi sağlanır.

## Kullanılan Teknolojiler

* **Python 3**
* **`socket` Kütüphanesi:** Ağ programlama ve TCP bağlantıları için.
* **`threading` Kütüphanesi:** Eş zamanlı işlemleri (concurrency) yönetmek için.

## Proje Yapısı

Proje iki ana dosyadan oluşmaktadır:

1.  `server.py`: Sunucu uygulamasını başlatan ve tüm istemci iletişimini yöneten ana betik.
2.  `client.py`: Sunucuya bağlanan ve kullanıcıların mesaj gönderip almasını sağlayan istemci betiği.

## Nasıl Çalıştırılır

Uygulamayı yerel makinenizde test etmek için aşağıdaki adımları izleyin.

### 1. Gereksinimler

* Python 3'ün sisteminizde kurulu olması gerekmektedir.

### 2. Sunucuyu Başlatma

Öncelikle sunucunun başlatılması gerekmektedir. Bir terminal veya komut istemi açın ve aşağıdaki komutu çalıştırın:

```bash
python server.py
