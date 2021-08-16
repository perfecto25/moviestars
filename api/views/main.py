from api import app
from loguru import logger

stars = {
    "Bruce Willis": {"movies": ["Die Hard", "Blind Date"]},
    "Arnold Shwarzenegger": {"movies": ["Terminator", "Conan", "Commando"]},
    "Sylvester Stallone": {"movies": ["Rambo", "Cobra", "Over the Top"]},
}


@app.get("/fetch")
async def fetch():
    """returns 80s movie stars"""
    logger.info("fetching movie stars to front end (Vue)")
    return stars
