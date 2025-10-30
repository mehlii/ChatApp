import socket
import threading

class ChatClient:
    """
    Nesne Tabanlı bir yaklaşımla tasarlanmış Chat İstemcisi.
    """
    
    def __init__(self, host='127.0.0.1', port=55555):
        """
        İstemciyi başlatan constructor metodu.
        """
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.username = input("Lütfen bir kullanıcı adı girin: ")

    def start(self):
        """
        Sunucuya bağlanır ve mesaj alma/gönderme thread'lerini başlatır.
        """
        try:

            self.client_socket.connect((self.host, self.port))
            print(f"Sunucuya bağlandı: {self.host}:{self.port}")

            self.client_socket.send(f"[{self.username}] sohbete katıldı.".encode('utf-8'))


            receive_thread = threading.Thread(target=self.receive_messages)
            receive_thread.daemon = True 
            receive_thread.start()

         
            self.send_messages()

        except ConnectionRefusedError:
            print("Sunucuya bağlanılamadı. Sunucunun çalıştığından emin olun.")
        except KeyboardInterrupt:
            print("\nÇıkış yapılıyor...")
        finally:
            self.client_socket.close()

    def receive_messages(self):
        """
        Sunucudan gelen mesajları sürekli dinler ve ekrana yazdırır.
        """
        while True:
            try:
                
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                   
                    print(f"\r{message}\n{self.username}: ", end="")
                else:
        
                    print("\rSunucuyla bağlantı kesildi.\n")
                    break
            except:

                print("\rBir hata oluştu, bağlantı kesiliyor...\n")
                break

    def send_messages(self):
        """
        Kullanıcıdan input alır ve sunucuya gönderir.
        """
        while True:

            message = input(f"{self.username}: ")
            

            if message.lower() == 'exit':
                break
                
            formatted_message = f"[{self.username}]: {message}"
            

            self.client_socket.send(formatted_message.encode('utf-8'))

if __name__ == "__main__":

    chat_client = ChatClient(host='127.0.0.1', port=55555)
    chat_client.start()