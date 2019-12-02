"""
creating models here
"""
from django import forms
from book_rental.models import BookCategory, Coustomer, Book


class BookCategoryForm(forms.ModelForm):
    """  creating forms for Book category"""

    class Meta:  # pylint: disable=too-few-public-methods
        """ creating class meta BookCategory"""
        model = BookCategory
        fields = '__all__'


class CoustomerForm(forms.ModelForm):
    """  creating forms for coustomer"""

    class Meta:  # pylint: disable=too-few-public-methods
        """ creating for coustomer form"""
        model = Coustomer
        fields = '__all__'


class BookForm(forms.ModelForm):
    """  creating forms for Book"""

    class Meta:  # pylint: disable=too-few-public-methods
        """creating class meta BookForm"""
        model = Book
        exclude = ('book_category',)
