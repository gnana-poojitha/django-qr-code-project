
# from django.shortcuts import render
# from .forms import QRCodeForm
# import qrcode
# from PIL import Image
# import os
# from django.conf import settings

# def generate_qr_code(request):
#     if request.method == 'POST':
#         form = QRCodeForm(request.POST, request.FILES)
#         if form.is_valid():
#             res_name = form.cleaned_data['restaurant_name']
#             url = form.cleaned_data['url']
#             fg_color = form.cleaned_data['fg_color']
#             bg_color = form.cleaned_data['bg_color']
#             logo_file = form.cleaned_data.get('logo')

#             # Create QR code
#             qr = qrcode.QRCode(
#                 version=1,
#                 error_correction=qrcode.constants.ERROR_CORRECT_H,
#                 box_size=10,
#                 border=4,
#             )
#             qr.add_data(url)
#             qr.make(fit=True)

#             img = qr.make_image(fill_color=fg_color, back_color=bg_color).convert('RGB')

#             # Add logo if provided
#             if logo_file:
#                 logo = Image.open(logo_file)
#                 # Resize logo
#                 basewidth = 80
#                 wpercent = (basewidth / float(logo.size[0]))
#                 hsize = int((float(logo.size[1]) * float(wpercent)))
#                 logo = logo.resize((basewidth, hsize), Image.LANCZOS)

#                 # Calculate position
#                 pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
#                 img.paste(logo, pos, mask=logo if logo.mode=='RGBA' else None)

#             # Save QR code
#             file_name = res_name.replace(" ", "_").lower() + '_menu.png'
#             file_path = os.path.join(settings.MEDIA_ROOT, file_name)
#             img = img.resize((330, 330))
#             img.save(file_path)

#             qr_url = os.path.join(settings.MEDIA_URL, file_name)

#             context = {
#                 'res_name': res_name,
#                 'qr_url': qr_url,
#                 'file_name': file_name,
#             }
#             return render(request, 'qr_result.html', context)

#     else:
#         form = QRCodeForm()

#     return render(request, 'generate_qr_code.html', {'form': form})









from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
from PIL import Image
from io import BytesIO
import base64

def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST, request.FILES)
        if form.is_valid():
            res_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']
            fg_color = form.cleaned_data['fg_color']
            bg_color = form.cleaned_data['bg_color']
            logo_file = form.cleaned_data.get('logo')

            # Create QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(url)
            qr.make(fit=True)

            img = qr.make_image(fill_color=fg_color, back_color=bg_color).convert('RGB')

            # Add logo if provided
            if logo_file:
                logo = Image.open(logo_file)
                basewidth = 80
                wpercent = (basewidth / float(logo.size[0]))
                hsize = int((float(logo.size[1]) * float(wpercent)))
                logo = logo.resize((basewidth, hsize), Image.LANCZOS)

                pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
                img.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)

            # Resize QR code
            img = img.resize((330, 330))

            # Save image to memory (instead of file system)
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            qr_base64 = base64.b64encode(buffer.getvalue()).decode()

            context = {
                'res_name': res_name,
                'qr_base64': qr_base64,  # pass base64 string
            }
            return render(request, 'qr_result.html', context)

    else:
        form = QRCodeForm()

    return render(request, 'generate_qr_code.html', {'form': form})

