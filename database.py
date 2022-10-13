import scraping

#MongoDB driver
import motor.motor_asyncio


client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
database = client.CL
collection = database.Matches


async def take_last_results():
    results = scraping.results()
    await collection.insert_many(results)
    print('OK')
    
async def show_one_pair(team):
    result = await collection.find_one({"Home Team": team})
    return result