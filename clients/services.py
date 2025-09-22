from authentication.services import JWTAndCookieServices
from authentication.models import CustomUser
from accessibility.models import Accessbility_Registration
from django.shortcuts import get_object_or_404

import logging
logger = logging.getLogger(__name__)

class Profile:
    @staticmethod
    def return_user(request, flag=None):
        token = request.COOKIES.get("access_token")
        paylod = JWTAndCookieServices.JWT_decode(token)        
        user = get_object_or_404(CustomUser, pk=paylod["user_id"])

        return user
    
    @staticmethod
    def assemble_profile(profile_data, user):
        access_registration = [
            {
             "id": reg.id,
             "accessibility": {
                 "id": reg.fk_id_tipo_acessibilidade.id,
                 "accessibility_name": reg.fk_id_tipo_acessibilidade.nome,
                 },
            }
            for reg in Accessbility_Registration.objects.filter(fk_id_cliente=user.client_profile.id)
        ]

        profile_data["client_profile"]["access_registration"] = access_registration

        return profile_data
    
    # @staticmethod
    # def updateProfile(data):
    #     logger.info("===========================================================")
    #     if data["client_profile"]["access_registration"]:
    #         access = data["client_profile"].pop["access_registration"]
    #         logger.info("=======================================================")