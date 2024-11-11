import requests
import os
from urllib.parse import urlparse

def convert_to_pdf_url(presentation_url):
    # Remove any trailing parameters or /edit
    base_url = presentation_url.split('/edit')[0].split('?')[0]
    # Add /export/pdf to the end
    return f"{base_url}/export/pdf"

def download_presentations(urls, output_folder="downloaded_presentations"):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for i, url in enumerate(urls, 1):
        try:
            # Convert URL to PDF download URL
            pdf_url = convert_to_pdf_url(url)
            
            # Extract presentation ID for filename
            presentation_id = urlparse(url).path.split('/')[-1]
            filename = f"presentation_{presentation_id}.pdf"
            filepath = os.path.join(output_folder, filename)
            
            # Download the PDF
            print(f"Downloading {i}/{len(urls)}: {filename}")
            response = requests.get(pdf_url)
            
            if response.status_code == 200:
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                print(f"Successfully downloaded: {filename}")
            else:
                print(f"Failed to download: {filename}")
                
        except Exception as e:
            print(f"Error downloading {url}: {str(e)}")

# Your list of URLs
urls = [
"https://docs.google.com/presentation/d/19NEzpJJ-a0lI-tdz9yC1kP-8Apt2oZm-918IsDiqgYQ","https://docs.google.com/presentation/d/1zt0yh_gzmfjCdB1y7DzTdwNSfTtepnQAtORH7PqebQM","https://docs.google.com/presentation/d/1G5k4HcjJ7C2fT_9xQdvpfWjKC4xQa--5FnwXPGf0nwg","https://docs.google.com/presentation/d/1Uty7XFuhRuCg3SoaSaViXzJhPTZDoYUV878L2I_pe_k","https://docs.google.com/presentation/d/1jjivjdvD4mx6qb4bd4rUKB6FDZbYtveJ5NKeyVeA1lk","https://docs.google.com/presentation/d/1AxuxcFWc_9U-gmdBRPGcEqE-7Q0-48hEw5Iupbama74","https://docs.google.com/presentation/d/1RJuwap1NZDYFUS7eiPy_SZu7oWHJladwuhKQpQcTjt8","https://docs.google.com/presentation/d/1LxnOVy_k13llkePdQIdBrZ5jEpgRmbrvMilD-ppRjlc","https://docs.google.com/presentation/d/1jVqC44HVViVtajnF18KsZ6MdIfseTfOSerfvxH4pzP0","https://docs.google.com/presentation/d/1WpISEkGajVCwARZy6w-XDF5sofm1cITUhfAlPUnnnos","https://docs.google.com/presentation/d/1bahvjVtbMcc2kuyzYQfQtD8EJyIiIkWnSALVSMuyQhI","https://docs.google.com/presentation/d/1CH4rsIIvu5pbmoWUNl9QdkPQYYkJc-ptX85CBhytlzM","https://docs.google.com/presentation/d/1XfRFqI5g6sM6LW2tWShnX-V2kVhBg6NJbIG6gvPtBn0","https://docs.google.com/presentation/d/18pzklQAvV94ODFpjeB60Rzj79wFHdkIB-ePWR_MeClk","https://docs.google.com/presentation/d/1zlmNjzu42WAEmyJFG2tYRZJIguExSFq5B__equ3-GaM","https://docs.google.com/presentation/d/1tAXgjwVKsnH7AR-iCvkDM-rQFwrg4OnKVZzqPixZWI8","https://docs.google.com/presentation/d/1uQYk0Hxhf0jhnp-aXxoIGNGM2w_yILMyukRctRPc9Uo","https://docs.google.com/presentation/d/1WJze5Odoy4ZR1vqPM8X6duaZ5GGm_D7SaYrtOa5RnsA","https://docs.google.com/presentation/d/1EGP_BWIbha4xQ4A5PJLAVIQaK6G0RbWZfrVDd0GmS08","https://docs.google.com/presentation/d/1XVJfoSYH2ItiD1rz9yvyEf_HelejbfkYxQgukbgclSY","https://docs.google.com/presentation/d/1Gyke5ZMrgcMuBTa7qHAoklWZB3yf_yqQAymK2nV-Nqs","https://docs.google.com/presentation/d/1NKWnXSJ8pUn1E2Cw6zidxMRuXf_aINKCpW7XpEkyz6c","https://docs.google.com/presentation/d/1mT-F0fxm-sVZj9EQS_E_QMv5SVfeCGptI9vsKpyp57Y","https://docs.google.com/presentation/d/1UHVEYtQhV7EQ74ETn5MvCsnRzsCzmp3MvXL84hXbw-g","https://docs.google.com/presentation/d/15afX6n25MybwUmm58M2xn8KqjQbMYHTQcTJ7u3h_I2M","https://docs.google.com/presentation/d/1tcKJNY-ultPxwaHtYn-kd-DV7aXcuBQm6resYvpoCkw","https://docs.google.com/presentation/d/1aleYBt-L8bwyaxw9tXPN3bMI5XxWxmpgfvvSEo9KxD0","https://docs.google.com/presentation/d/1MqmOxfh1c6gS4hk9hvuRR_hWXWTnCIXMqLGXwRX4Pvk","https://docs.google.com/presentation/d/1P1Uc8phy1GW1M4A8PA7mJJMWqb2QgOfewwwB1wMnFlU","https://docs.google.com/presentation/d/11vRyW0ZPrsxUhRHCBgkygy01PlL1amB66n9FZQN03wo","https://docs.google.com/presentation/d/1sqpg9sM-0719KGcWzYmmrWlj0azaafgIAiM8U98jKi4","https://docs.google.com/presentation/d/1nE_oD8Mx6tRcO6zOnz7KbSxCtaZpaoDlcPhKzfNXrqI","https://docs.google.com/presentation/d/14jNEZC-YKUuxIr3Cxsvz1Kb6eX0jCjvjevb1zD8NRj4","https://docs.google.com/presentation/d/1wSTXwNB-D75VbHCtKqnr7QlOQtV-3wg6vTLNpNw7Qwk","https://docs.google.com/presentation/d/13TE3w603C6zt1q5vWRL9WmbwxkG0VjFluIIHSbV0qNU","https://docs.google.com/presentation/d/1k4tgpf7xaW-uhlHYlp3izZRYtBGMYPVRlHCmmpN6QXQ","https://docs.google.com/presentation/d/1QFwbmMVE0Wlvg-gnWnemTxRX_t7h6IlhCQU69dcAkaA","https://docs.google.com/presentation/d/1MmnYUoi-4Wyt6_3BcBdt_WkrL1XECZ9ypCyUmhW7e2U",
]

# Download the presentations
download_presentations(urls)
