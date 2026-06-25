from database.db import create_database
from services.queue_service import QueueService

create_database()

queue = QueueService()

result = queue.import_excel()

print(result)
