from time import time
from django.utils.translation import gettext_lazy as _

from django.conf import settings
PROMOCODE_ERRORS = {
    'not_exist_or_not_suitable': _("Bu promokod ya mövcud deyil, ya da bu servizə uyğun deyil."),
    'not_suitable_for_warehouse': _("Bu promokod sizin anbara uyğun deyil."),
    'not_suitable_for_country': _("Bu promokod bu ölkə üçün keçərli deyil."),
    'deactivated_or_crossed_deadline': _("Bu promokod artıq keçərli deyil, ya deaktiv olunub, ya da bitmə tarixini keçib."),
    'general_limit_is_over': _("Bu promokodun ümumi olaraq istifadə limiti bitib."),
    'user_limit_is_over': _("Sizin üçün bu promokodun istifadə limiti bitib."),
    'not_suitable_for_web': _("Bu promokod WEB üçün keçərli deyil, mobil applər üçün keçərlidir."),
    'not_suitable_for_3': _("Bu promokod iOS üçün keçərli deyil, Android və ya WEB üçün keçərlidir."),# 3 - iOS
    'not_suitable_for_2': _("Bu promokod Andorid üçün keçərli deyil, iOS və ya WEB üçün keçərlidir."), # 2 - Android    
    'not_suitable_for_1': _("Bu promokod WEB üçün keçərli deyil, mobil applər üçün keçərlidir."),# 3 - iOS
    'promocode_is_disabled_for_orders_from_setting': _("Promokod özəlliyi sifarişlər üçün bağlanılıb."), 
    'promocode_is_disabled_for_declarations_from_setting': _("Promokod özəlliyi bağlamalar üçün bağlanılıb."), 
    'promocode_is_disabled_for_courier_from_setting': _("Promokod özəlliyi kuryer sifarişi üçün bağlanılıb."), 
    'promocode_is_disabled_for_country': _("Promokod özəlliyi bu ölkə üçün bağlanılıb."), 
}
