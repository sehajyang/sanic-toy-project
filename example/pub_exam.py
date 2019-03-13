import asyncio

from room import Room

if __name__ == '__main__':
    async def main():
        room = Room(10)
        await room.join_room()
        await room.send_message('hello!')


    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())