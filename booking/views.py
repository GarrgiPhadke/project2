from django.shortcuts import render
from booking.models import Booking
from django.core.validators import ValidationError
from django.utils import timezone

def booking(request):
    if request.method == 'POST':
        # Collect data from POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        location = request.POST.get('location', 'No location')
        message = request.POST.get('message', 'No message')
        submitted_date = request.POST.get('submitted_date')
        submitted_time = request.POST.get('submitted_time')

        # Validate inputs
        errors = []
        if not name:
            errors.append('Name is required.')
        if not email:
            errors.append('Email is required.')
        if not phone:
            errors.append('Phone number is required.')

        # Validate email and phone formats
        from django.core.validators import EmailValidator, RegexValidator
        
        email_validator = EmailValidator()
        phone_validator = RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message="Phone number must be in the format: '+999999999'. Up to 15 digits allowed."
        )

        try:
            email_validator(email)
        except ValidationError as e:
            errors.append(f"Invalid email format: {e.message}")

        try:
            phone_validator(phone)
        except ValidationError as e:
            errors.append(f"Invalid phone format: {e.message}")

        if not submitted_date:
            submitted_date = timezone.now().date()
       
        if errors:
            return render(request, 'booking.html', {'errors': errors})

        # Save to the database
        ins = Booking(
            name=name, email=email, phone=phone, location=location, 
            message=message, submitted_date=submitted_date,
       
        )
        ins.save()
        return render(request, 'booking.html', {'success': True})

    return render(request, 'booking.html')
