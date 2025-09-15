__all__ = ("router",)

from .list_vievs import router
from .detail_views import router as detail_router

router.include_router(detail_router)
