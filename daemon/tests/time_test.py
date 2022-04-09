
import dbus

def main():
    bus = dbus.SessionBus()

    remote_object = bus.get_object("com.github.jeysonflores.hasher.Service", "/com/github/jeysonflores/hasher/Service")

    iface = dbus.Interface(remote_object, "com.github.jeysonflores.hasher.Service")

    regexes = iface.Hash("/home/jeyson/Descargas/test.zip", 11)
    print(regexes)

if __name__ == '__main__':
    main()