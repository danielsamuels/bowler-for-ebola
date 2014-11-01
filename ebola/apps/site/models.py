from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.timezone import now

import cv2
from PIL import Image as PILImage
import StringIO
from sorl.thumbnail import ImageField
import uuid


def upload_path(instance, filename):
    return 'uploads/files/{}.{}'.format(
        instance.uuid,
        filename.split('.')[-1]
    )


def processed_upload_path(instance, filename):
    return 'uploads/files/{}_processed.{}'.format(
        instance.uuid,
        filename.split('.')[-1]
    )


class Image(models.Model):

    uuid = models.CharField(
        "UUID",
        max_length=36,
        primary_key=True,
        default=uuid.uuid4
    )

    image = ImageField(
        upload_to=upload_path
    )

    processed = ImageField(
        upload_to=processed_upload_path,
        blank=True,
        null=True,
    )

    ip_address = models.GenericIPAddressField(
        "IP address",
        blank=True,
        null=True,
    )

    timestamp = models.DateTimeField(
        auto_now_add=True,
        default=now
    )

    def get_absolute_url(self):
        return reverse('image:detail', kwargs={
            'uuid': str(self.uuid)
        })

    def save(self, *args, **kwargs):
        # Save the object.
        super(Image, self).save(*args, **kwargs)

        if not self.processed:
            # Run image processing.
            face = cv2.imread(self.image.file.file.name)

            pil_face = PILImage.open(self.image.file.file.name)
            pil_hat = PILImage.open('ebola/static/img/bowler.png')

            cascade = cv2.CascadeClassifier('ebola/static/other/lbpcascade_frontalface.xml')
            faces = cascade.detectMultiScale(face, scaleFactor=1.2)

            if len(faces) > 0:
                for (x, y, w, h) in faces:
                    base_size = pil_hat.size
                    ratio = float(base_size[0]) / float(base_size[1])
                    increase = 1.3
                    new_size = (int(w*increase), int((w*increase) / ratio))

                    # Desired width
                    pil_hat = pil_hat.resize(new_size, PILImage.ANTIALIAS)

                    pil_face.paste(pil_hat, (x + ((w - pil_hat.size[0]) / 2), y - pil_hat.size[1] + (h/4)), pil_hat)

                thumb_io = StringIO.StringIO()
                pil_face.save(thumb_io, format='JPEG')

                thumb_file = InMemoryUploadedFile(
                    thumb_io,
                    None,
                    '{}_processed.jpg'.format(
                        self.uuid
                    ),
                    'image/jpeg',
                    thumb_io.len,
                    None
                )

                self.processed = thumb_file
                self.save()

    class Meta:
        ordering = ('-timestamp',)
