import bluetooth

def scan_paired_devices():
    paired_devices = bluetooth.discover_devices(lookup_names=True, lookup_class=True, device_id=-1, duration=8, flush_cache=True, lookup_oui=True)

    if paired_devices:
        print("Paired Bluetooth Devices:")
        for addr, name, _ in paired_devices:
            print(f"Device Name: {name}")
            print(f"Device Address: {addr}")
            print("----------------------")
    else:
        print("No paired Bluetooth devices found.")

if __name__ == "__main__":
    scan_paired_devices()
