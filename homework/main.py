# Создание записи (Create)
new_client = Client.objects.create(
    name="Иван Иванов",
    email="ivan@example.com",
    phone_number="123-456-7890",
    address="ул. Кулакова, д. 1",
    registration_date=timezone.now()
)

# Чтение записи (Read)
all_clients = Client.objects.all()
client = Client.objects.get(id=1)

# Обновление записи (Update)
client = Client.objects.get(id=1)
client.name = "Новое имя"
client.save()

# Удаление записи (Delete)
client = Client.objects.get(id=1)
client.delete()

