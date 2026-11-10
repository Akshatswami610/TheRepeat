
from urllib.parse import quote

from django.conf import settings
from storages.backends.s3 import S3Storage


class SupabaseMediaStorage(S3Storage):

    def __init__(self, **kwargs):
        kwargs.setdefault(
            "bucket_name",
            settings.SUPABASE_MEDIA_BUCKET
        )
        kwargs.setdefault(
            "endpoint_url",
            settings.SUPABASE_S3_ENDPOINT
        )
        kwargs.setdefault(
            "region_name",
            settings.SUPABASE_S3_REGION
        )
        kwargs.setdefault(
            "access_key",
            settings.SUPABASE_S3_ACCESS_KEY
        )
        kwargs.setdefault(
            "secret_key",
            settings.SUPABASE_S3_SECRET_KEY
        )

        kwargs.setdefault("addressing_style", "path")
        kwargs.setdefault("signature_version", "s3v4")
        kwargs.setdefault("querystring_auth", False)
        kwargs.setdefault("file_overwrite", False)

        super().__init__(**kwargs)

    def url(self, name, parameters=None, expire=None, http_method=None):
        name = quote(name.lstrip("/"), safe="/")

        return (
            f"{settings.SUPABASE_URL}/storage/v1/object/public/"
            f"{settings.SUPABASE_MEDIA_BUCKET}/{name}"
        )
