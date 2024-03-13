import random
import time

# Функция для генерации сетевого трафика
def generate_traffic():
    devices = ['Mobile1', 'Mobile2', 'Mobile3']
    services = ['HTTP', 'SSH', 'DNS', 'FTP', 'SMTP']
    return {
        'device': random.choice(devices),
        'service': random.choice(services),
        'timestamp': time.time()
    }

# Функция для обнаружения подозрительной активности
def detect_suspicious_activity(traffic):
    # Правило обнаружения 1: если устройство отправляет слишком много запросов за короткий промежуток времени
    device = traffic['device']
    current_time = traffic['timestamp']
    if device in traffic_count:
        if current_time - traffic_count[device]['timestamp'] < 5:
            traffic_count[device]['count'] += 1
            if traffic_count[device]['count'] > 3:
                print(f"Suspicious activity detected from {device}!")
        else:
            traffic_count[device] = {'timestamp': current_time, 'count': 1}
    else:
        traffic_count[device] = {'timestamp': current_time, 'count': 1}

    # Правило обнаружения 2: если устройство обращается к неожиданным сервисам
    if traffic['service'] not in allowed_services[device]:
        print(f"Suspicious activity detected from {device}: accessing unexpected service {traffic['service']}!")

# Функция для вывода результатов обнаружения
def output_results(result):
    print(result)

if __name__ == "__main__":
    traffic_count = {}
    allowed_services = {
        'Mobile1': ['HTTP', 'SSH', 'DNS'],
        'Mobile2': ['HTTP', 'DNS'],
        'Mobile3': ['SSH', 'DNS']
    }
    # Симуляция сетевого трафика в течение 2 часов
    start_time = time.time()
    while time.time() - start_time < 7200:
        traffic_data = generate_traffic()
        detect_suspicious_activity(traffic_data)
        time.sleep(0.5)  # Имитация интервала между запросами
