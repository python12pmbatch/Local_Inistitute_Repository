from django import forms


class ProductForm(forms.Form):
    Product_Number = forms.IntegerField(
        label='Enter Your Product Number',
        widget= forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Number'
            }
        )
    )
    Product_Name = forms.CharField(
        label='Enter Your Product Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Name'
            }
        )
    )
    Product_Cost = forms.IntegerField(
        label = 'Enter Your Product Cost',
        widget= forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Cost'
            }

        )
    )
    Product_Color = forms.CharField(
        label='Enter Your Product Color',
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Color'
            }
        )
    )
    Product_Class = forms.CharField(
        label='Enter Your Product Class',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Class'
            }
        )
    )
    Number_Of_Products = forms.IntegerField(
        label='Enter Number Of Products',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Number Of Products'
            }
        )
    )
    Customer_Name = forms.CharField(
        label='Enter Customer Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Customer Name'
            }
        )
    )
    Customer_Number = forms.IntegerField(
        label='Enter Customer Number',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Mobile Number'
            }
        )
    )
    Email_Id = forms.EmailField(
        label='Enter Customer Email Id',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Email Id'
            }
        )
    )

class UpdateForm(forms.Form):
    Product_Number = forms.IntegerField(
        label='Enter Product Id',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Id to Update',
            }
        )
    )
    Product_Cost = forms.IntegerField(
        label='Enter Product Cost',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'New Product cost'
            }
        )
    )

class DeleteForm(forms.Form):
    Product_Number = forms.IntegerField(
        label='Enter product Id',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product ID to delete'
            }
        )
    )

