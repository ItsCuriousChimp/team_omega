from django.utils import timezone
from ..dto.heartBeat_dto import Health_Check_Dto


class HeartBeat_Repository:
    def heartBeat_repository_reponse(self) -> Health_Check_Dto:
        healthCheck = Health_Check_Dto(timezone.now())
        return healthCheck
