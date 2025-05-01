
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def simulate_sir_with_mutation(N=10000, I0=1, R0=0, beta=0.3, gamma=0.1, mu_rate=0.02, days=160):
    S, I, R, M = [N - I0 - R0], [I0], [R0], [0]
    for t in range(1, days):
        new_infected = beta * S[-1] * I[-1] / N
        new_recovered = gamma * I[-1]
        new_mutations = mu_rate * I[-1]

        S.append(S[-1] - new_infected)
        I.append(I[-1] + new_infected - new_recovered)
        R.append(R[-1] + new_recovered)
        M.append(M[-1] + new_mutations)

    return S, I, R, M

def show_sir_simulation():
    st.subheader("📊 Infection Spread & Mutation Simulation (SIR+M)")

    col1, col2 = st.columns(2)
    with col1:
        N = st.slider("Total Population (N)", 1000, 100000, 10000, 1000)
        I0 = st.slider("Initial Infected (I₀)", 1, 1000, 10)
        beta = st.slider("Infection Rate (β)", 0.05, 1.0, 0.3)
    with col2:
        gamma = st.slider("Recovery Rate (γ)", 0.01, 1.0, 0.1)
        mu = st.slider("Mutation Rate (μ)", 0.0, 0.1, 0.02)
        days = st.slider("Simulation Days", 30, 365, 160)

    S, I, R, M = simulate_sir_with_mutation(N, I0, 0, beta, gamma, mu, days)
    t = np.arange(days)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(t, S, label="Susceptible", color="blue")
    ax.plot(t, I, label="Infected", color="orange")
    ax.plot(t, R, label="Recovered", color="green")
    ax.plot(t, M, label="Mutations (accumulated)", color="red", linestyle="--")
    ax.set_xlabel("Days")
    ax.set_ylabel("Population")
    ax.set_title("SIR Model with Mutation Overlay")
    ax.legend()
    st.pyplot(fig)
