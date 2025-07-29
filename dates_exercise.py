# Exercício: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime
from dateutil.relativedelta import relativedelta

loan_value = 1_000_000
loan_date = datetime(2020, 12, 20)
delta_years = relativedelta(years=5)
loan_final_date = loan_date + delta_years

installment_date_list = []
installment_date = loan_date

while installment_date < loan_final_date:
    installment_date_list.append(installment_date)
    installment_date += relativedelta(months=+1)

installment_qtd = len(installment_date_list)
installment_value = loan_value / installment_qtd
print(installment_value)

for date in installment_date_list:
    print(date.strftime('%d/%m/%Y'), f'R$ {installment_value:,.2f}')

print()
print(
    f'You\'ve taken R${loan_value:,.2f} to pay in {delta_years.years} years '
    f'({installment_qtd} months) in installments of '
    f'R${installment_value:,.2f}.'
)
