import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from pulp import LpMaximize, LpMinimize, LpProblem, LpVariable, lpSum, LpStatus

# Título de la aplicación
st.title("Resolución de Ejercicios de Programación Entera y Lineal")

# Sidebar para seleccionar el ejercicio
exercise = st.sidebar.selectbox("Selecciona un ejercicio", ["Ejercicio 8.1", "Ejercicio 8.2", "Ejercicio 8.3", "Ejercicio 8.4", "Ejercicio 8.5"])

# Función para resolver el Ejercicio 8.1 (Método de Dakin)
def solve_exercise_8_1():
    st.subheader("Ejercicio 8.1 - Método de Dakin para Programación Entera")
    # Definir el problema
    prob = LpProblem("Ejercicio_8.1", LpMaximize)
    
    # Variables
    x1 = LpVariable("x1", lowBound=0, cat="Integer")
    x2 = LpVariable("x2", lowBound=0, cat="Integer")
    x3 = LpVariable("x3", lowBound=0, cat="Integer")
    
    # Función objetivo
    prob += 4 * x1 + 3 * x2 + x3
    
    # Restricciones
    prob += 4 * x1 + 2 * x2 + x3 <= 10
    prob += 3 * x1 + 4 * x2 + 2 * x3 <= 14
    prob += 2 * x1 + x2 + 3 * x3 <= 7
    
    # Resolver el problema
    prob.solve()
    
    # Resultados
    st.write(f"Estado de la solución: {LpStatus[prob.status]}")
    st.write(f"x1 = {x1.varValue}, x2 = {x2.varValue}, x3 = {x3.varValue}")
    st.write(f"Valor óptimo: {prob.objective.value()}")
    
    # Gráfico
    fig, ax = plt.subplots()
    ax.bar(["x1", "x2", "x3"], [x1.varValue, x2.varValue, x3.varValue])
    ax.set_ylabel("Valor de las Variables")
    st.pyplot(fig)

# Función para resolver el Ejercicio 8.2
def solve_exercise_8_2():
    st.subheader("Ejercicio 8.2 - Solver de Programación Entera")
    # Definir el problema
    prob = LpProblem("Ejercicio_8.2", LpMaximize)
    
    # Variables
    x1 = LpVariable("x1", lowBound=0, cat="Integer")
    x2 = LpVariable("x2", lowBound=0, cat="Integer")
    
    # Función objetivo
    prob += 5 * x1 + 2 * x2
    
    # Restricciones
    prob += 3 * x1 + 2 * x2 <= 12
    prob += 4 * x1 - x2 <= 8
    
    # Resolver el problema
    prob.solve()
    
    # Resultados
    st.write(f"Estado de la solución: {LpStatus[prob.status]}")
    st.write(f"x1 = {x1.varValue}, x2 = {x2.varValue}")
    st.write(f"Valor óptimo: {prob.objective.value()}")
    
    # Gráfico
    fig, ax = plt.subplots()
    ax.bar(["x1", "x2"], [x1.varValue, x2.varValue])
    ax.set_ylabel("Valor de las Variables")
    st.pyplot(fig)

# Función para resolver el Ejercicio 8.3 (Planos de Corte)
def solve_exercise_8_3():
    st.subheader("Ejercicio 8.3 - Planos de Corte")
    # Definir el problema
    prob = LpProblem("Ejercicio_8.3", LpMinimize)
    
    # Variables
    x = LpVariable("x", lowBound=0, cat="Integer")
    y = LpVariable("y", lowBound=0, cat="Integer")
    
    # Función objetivo
    prob += x - y
    
    # Restricciones
    prob += 3 * x + 4 * y <= 6
    prob += x - y <= 1
    
    # Resolver el problema
    prob.solve()
    
    # Resultados
    st.write(f"Estado de la solución: {LpStatus[prob.status]}")
    st.write(f"x = {x.varValue}, y = {y.varValue}")
    st.write(f"Valor óptimo: {prob.objective.value()}")
    
    # Gráfico
    fig, ax = plt.subplots()
    ax.bar(["x", "y"], [x.varValue, y.varValue])
    ax.set_ylabel("Valor de las Variables")
    st.pyplot(fig)

# Función para resolver el Ejercicio 8.4 (Planos de Corte de Gomory)
def solve_exercise_8_4():
    st.subheader("Ejercicio 8.4 - Planos de Corte de Gomory")
    # Definir el problema
    prob = LpProblem("Ejercicio_8.4", LpMaximize)
    
    # Variables
    x1 = LpVariable("x1", lowBound=0, cat="Integer")
    x2 = LpVariable("x2", lowBound=0, cat="Integer")
    
    # Función objetivo
    prob += 2 * x1 + x2
    
    # Restricciones
    prob += 2 * x1 + 3 * x2 <= 7
    prob += x1 + x2 <= 5
    
    # Resolver el problema
    prob.solve()
    
    # Resultados
    st.write(f"Estado de la solución: {LpStatus[prob.status]}")
    st.write(f"x1 = {x1.varValue}, x2 = {x2.varValue}")
    st.write(f"Valor óptimo: {prob.objective.value()}")
    
    # Gráfico
    fig, ax = plt.subplots()
    ax.bar(["x1", "x2"], [x1.varValue, x2.varValue])
    ax.set_ylabel("Valor de las Variables")
    st.pyplot(fig)

# Función para resolver el Ejercicio 8.5 (Selección de Proyectos de Inversión)
def solve_exercise_8_5():
    st.subheader("Ejercicio 8.5 - Selección de Proyectos de Inversión")
    # Definir el problema
    prob = LpProblem("Ejercicio_8.5", LpMaximize)
    
    # Variables
    x1 = LpVariable("x1", cat="Binary")
    x2 = LpVariable("x2", cat="Binary")
    x3 = LpVariable("x3", cat="Binary")
    
    # Función objetivo
    prob += 100 * x1 + 150 * x2 + 200 * x3
    
    # Restricciones
    prob += 50 * x1 + 60 * x2 + 80 * x3 <= 150  # Presupuesto total
    
    # Resolver el problema
    prob.solve()
    
    # Resultados
    st.write(f"Estado de la solución: {LpStatus[prob.status]}")
    st.write(f"x1 = {x1.varValue}, x2 = {x2.varValue}, x3 = {x3.varValue}")
    st.write(f"Valor óptimo: {prob.objective.value()}")
    
    # Gráfico
    fig, ax = plt.subplots()
    ax.bar(["x1", "x2", "x3"], [x1.varValue, x2.varValue, x3.varValue])
    ax.set_ylabel("Proyectos Seleccionados")
    st.pyplot(fig)

# Lógica para seleccionar y ejecutar el ejercicio
if exercise == "Ejercicio 8.1":
    solve_exercise_8_1()
elif exercise == "Ejercicio 8.2":
    solve_exercise_8_2()
elif exercise == "Ejercicio 8.3":
    solve_exercise_8_3()
elif exercise == "Ejercicio 8.4":
    solve_exercise_8_4()
elif exercise == "Ejercicio 8.5":
    solve_exercise_8_5()
