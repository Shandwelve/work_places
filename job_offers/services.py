from .models import JobOffer


def create(position: str, company: str):
    offer = JobOffer(position=position, company=company)
    offer.save()
