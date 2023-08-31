import csv
from statistics import mean, stdev

# Carregar os dados do arquivo CSV
def load_data(file_name):
    data = []
    with open(file_name, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

# Exibir menu principal
def show_main_menu():
    print("Escolha uma opção:")
    print("1. Informações descritivas")
    print("2. Filtrar registros")
    print("3. Realizar agrupamento de registros")
    print("4. Sair")

# Exibir informações descritivas
def show_descriptive_info(data):
    num_records = len(data) - 1
    num_columns = len(data[0])
    column_names = data[0]
    
    print("Informações descritivas:")
    print(f"Quantidade de registros: {num_records}")
    print(f"Quantidade de colunas: {num_columns}")
    print(f"Nome e tipo de cada coluna:")
    for col_name in column_names:
        print(col_name)
    
    numeric_columns = []
    for col_index in range(6, num_columns):
        try:
            numeric_col = [float(row[col_index]) for row in data[1:]]
            numeric_columns.append(numeric_col)
        except ValueError:
            pass
    
    for i, col_name in enumerate(column_names[6:]):
        if i < len(numeric_columns):
            col_values = numeric_columns[i]
            max_value = max(col_values)
            min_value = min(col_values)
            avg_value = mean(col_values)
            print(f"Coluna: {col_name}")
            print(f"  Valor máximo: {max_value:.2f}")
            print(f"  Valor mínimo: {min_value:.2f}")
            print(f"  Valor médio: {avg_value:.2f}")
    print()

# Filtrar registros
def filter_records(data):
    column_names = data[0]
    
    print("Filtrar registros:")
    print("Escolha a coluna para a condição de filtragem:")
    for i, col_name in enumerate(column_names):
        print(f"{i}. {col_name}")
    
    col_choice = int(input("Digite o número da coluna: "))
    chosen_column = column_names[col_choice]
    chosen_values = input("Digite os valores para a condição (separados por vírgula): ").split(',')
    chosen_test = input("Digite o teste de comparação (ex: >, <, =, >=, <=, !=): ")
    
    filtered_data = [data[0]]  # Header
    for row in data[1:]:
        if chosen_test == '=':
            if row[col_choice] in chosen_values:
                filtered_data.append(row)
        else:
            if eval(f"float(row[col_choice]) {chosen_test} float(chosen_values[0])"):
                filtered_data.append(row)
    
    return filtered_data

# Realizar agrupamento de registros
def group_and_apply(data):
    column_names = data[0]
    
    print("Agrupar registros:")
    print("Escolha a coluna para agrupamento:")
    for i, col_name in enumerate(column_names):
        print(f"{i}. {col_name}")
    
    col_choice = int(input("Digite o número da coluna: "))
    group_column = column_names[col_choice]
    
    print("Escolha a função de agrupamento:")
    print("1. Máximo")
    print("2. Mínimo")
    print("3. Média")
    print("4. Desvio padrão")
    func_choice = int(input("Digite o número da função: "))
    
    grouped_data = {row[col_choice]: [] for row in data[1:]}
    for row in data[1:]:
        grouped_data[row[col_choice]].append(float(row[6:][col_choice]))
    
    print(f"Resultado do agrupamento por '{group_column}':")
    for value, values in grouped_data.items():
        if func_choice == 1:
            result = max(values)
            func_name = "Máximo"
        elif func_choice == 2:
            result = min(values)
            func_name = "Mínimo"
        elif func_choice == 3:
            result = mean(values)
            func_name = "Média"
        elif func_choice == 4:
            result = stdev(values)
            func_name = "Desvio padrão"
        print(f"{group_column} '{value}': {func_name} = {result:.2f}")
    print()

def main():
    file_name = "fipe.csv"
    data = load_data(file_name)
    
    while True:
        show_main_menu()
        choice = input("Digite o número da opção: ")
        
        if choice == '1':
            show_descriptive_info(data)
        elif choice == '2':
            filtered_data = filter_records(data)
            for row in filtered_data:
                print(', '.join(row))
        elif choice == '3':
            group_and_apply(data)
        elif choice == '4':
            break
        else:
            print("Opção inválida. Digite novamente.")

if __name__ == "__main__":
    main()