import pandas as pd
import matplotlib.pyplot as plt

def load_data(path="data/students.json"):
    return pd.read_json(path)


def plot_average_marks(df):
    avg_marks = df["average_marks"]

    plt.figure()
    plt.hist(avg_marks, bins=10)
    plt.title("Average Marks Distribution")
    plt.xlabel("Marks")
    plt.ylabel("Number of Students")

    return plt


def plot_performance_counts(df):
    counts = df["performance"].value_counts()

    plt.figure()
    counts.plot(kind="bar")
    plt.title("Performance Distribution")
    plt.xlabel("Category")
    plt.ylabel("Count")

    return plt


def plot_attendance(df):
    plt.figure()
    plt.scatter(df["attendance_percentage"], df["average_marks"])
    plt.xlabel("Attendance %")
    plt.ylabel("Average Marks")
    plt.title("Attendance vs Marks")

    return plt