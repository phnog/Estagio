from datetime import timedelta, date

valortotal = float(input("Digite o valor total a ser parcelado: "))
nparcelas = int(input("Digite o numero de parcelas: "))
n = 0; 
parcelamento = valortotal/nparcelas
print(parcelamento)

Date_required = date.today() + timedelta(days=30)


while n < nparcelas:
    print("A parcela ser paga e no valor de : ","{:.2f}".format(parcelamento), "R$")
    print("A data de vencimento é ",Date_required)
    Date_required = Date_required + timedelta(days=30)
    
    n = n + 1