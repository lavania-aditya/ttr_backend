import cloudinary.uploader


def upload_image_to_cloudinary(image_file):
    """Upload an image to Cloudinary and return the secure URL."""
    result = cloudinary.uploader.upload(image_file)
    return result.get("secure_url")
