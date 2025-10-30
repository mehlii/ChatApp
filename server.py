import socket
import threading

class ChatServer:
    """
    Nesne Tabanlı bir yaklaşımla tasarlanmış çok kullanıcılı Chat Sunucusu.
    """

    clients = []
    

    lock = threading.Lock()

    def __init__(self, host='127.0.0.1', port=55555):
        """
        Sunucuyu başlatan constructor metodu.
        """
        self.host = host
        self.port = port

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"Sunucu {self.host}:{self.port} adresinde başlatılıyor...")

    def start(self):
        """
        Sunucuyu dinleme moduna alır ve bağlantıları kabul etmeye başlar.
        """

        self.server_socket.bind((self.host, self.port))

        self.server_socket.listen()
        print(f"Sunucu dinlemede...")


        try:
            while True:

                client_socket, address = self.server_socket.accept()
                print(f"{address} adresinden yeni bir bağlantı kabul edildi.")
                

                with self.lock:
                    self.clients.append(client_socket)
                

                client_thread = threading.Thread(target=self.handle_client, args=(client_socket, address))
                client_thread.start()
        except KeyboardInterrupt:
            print("\nSunucu kapatılıyor...")
        finally:
            self.server_socket.close()

    def handle_client(self, client_socket, address):
        """
        Her bir istemci bağlantısını ayrı bir thread'de yönetir.
        """
        try:
            while True:

                message = client_socket.recv(1024)
                

                if not message:
                    print(f"{address} bağlantıyı kesti.")
                    break
                    

                self.broadcast(message, client_socket)
        except ConnectionResetError:
            print(f"{address} bağlantıyı aniden kesti.")
        finally:

            self.remove_client(client_socket)

    def broadcast(self, message, sender_socket):
        """
        Bir mesajı, gönderen hariç tüm bağlı istemcilere gönderir.
        """
        with self.lock:
            for client in self.clients:

                if client != sender_socket:
                    try:
                        client.send(message)
                    except:

                        self.remove_client(client)

    def remove_client(self, client_socket):
        """
        Bağlantısı kesilen istemciyi güvenli bir şekilde listeden kaldırır.
        """
        with self.lock:
            if client_socket in self.clients:
                self.clients.remove(client_socket)
                client_socket.close()


if __name__ == "__main__":

    chat_server = ChatServer(host='127.0.0.1', port=55555)
    chat_server.start()