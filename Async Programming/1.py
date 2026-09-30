import asyncio

async def download_policy():
    print("Downloading...")
    await asyncio.sleep(3)
    print("Downloaded")

async def send_email():
    print("Sending email...")
    await asyncio.sleep(2)
    print("Email sent")

async def main():
    await asyncio.gather(
        download_policy(),
        send_email()
    )

asyncio.run(main())