import streamlit as st

def main():
    st.title('Knapsack Problem Solver')
    
    capacity = st.number_input('Capacidad de la mochila', min_value=0, step=1)
    values_input = st.text_input('Valores (separados por coma)', '60,100,120')
    weights_input = st.text_input('Pesos (separados por coma)', '10,20,30')

    if st.button('Calcular'):
        try:
            values = list(map(int, values_input.split(',')))
            weights = list(map(int, weights_input.split(',')))

            if len(values) != len(weights):
                st.error('La cantidad de valores y pesos deben ser iguales.')
                return

            n = len(values)
            dp = [[0] * (capacity + 1) for _ in range(n + 1)]

            for i in range(1, n + 1):
                for w in range(1, capacity + 1):
                    if weights[i - 1] <= w:
                        dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
                    else:
                        dp[i][w] = dp[i - 1][w]

            max_value = dp[n][capacity]
            st.write(f'Valor máximo que se puede obtener: {max_value}')

        except ValueError:
            st.error('Error: Asegúrate de ingresar solo números separados por coma.')

if __name__ == "__main__":
    main()
