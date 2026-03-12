import os
import random
import time
import tkinter
from tkinter import *
from tkinter import Tk
from tkinter import messagebox
from tkinter.ttk import Combobox
import hashlib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import csv
import tracemalloc

class Main_GUI:


    def __init__(self, root):
        self.file_path = StringVar()
        self.noofnodes = StringVar()

        self.LARGE_FONT = ("Algerian", 16)
        self.text_font = ("Constantia", 15)
        self.text_font1 = ("Constantia", 10)

        self.frame_font = ("", 9)
        self.frame_process_res_font = ("", 12)
        self.root = root
        self.feature_value = StringVar()

        label_heading = tkinter.Label(root,
                                      text="LH-CN and ST-GTN Enabled Energy-Aware Data Placement and Adaptive Caching in Edge–Fog–Cloud Computing",
                                      fg="#8B2252", bg="#79CDCD", font=self.LARGE_FONT)
        label_heading.place(x=0, y=0)

        self.label_initialization = LabelFrame(root, text="System Initialization and Configuration", bg="#79CDCD", fg="#8B5A2B", font=self.frame_font)
        self.label_initialization.place(x=10, y=30, width=220, height=50)
        self.number_edge = ["100", "200", "300", "400", "500"]
        self.cmb_number_edge = Combobox(root, width=6, height=30)
        self.cmb_number_edge["values"] = self.number_edge
        self.cmb_number_edge.set("Edges")
        self.cmb_number_edge.grid(column=1, row=5)
        self.cmb_number_edge.place(x=20, y=50)
        self.cmb_number_edge.configure(state='readonly')

        self.number_fog = ["10", "20", "30", "40", "50"]
        self.cmb_number_fog = Combobox(root, width=6, height=30)
        self.cmb_number_fog["values"] = self.number_fog
        self.cmb_number_fog.set("Fog")
        self.cmb_number_fog.grid(column=1, row=5)
        self.cmb_number_fog.place(x=90, y=50)
        self.cmb_number_fog.configure(state='readonly')

        self.btn_edge_fog_initialization = Button(root, text="Initialize", bg="#1E90FF", fg="#fff", font=self.text_font1, width=7, command=self.edge_fog_initialization)
        self.btn_edge_fog_initialization.place(x=160, y=50)

        self.label_data_collection = LabelFrame(root, text="Data Collection", bg="#79CDCD", fg="#8B5A2B", font=self.frame_font)
        self.label_data_collection.place(x=240, y=30, width=170, height=50)
        self.number_task = ["Task 500", "Task 1000", "Task 1500", "Task 2000", "Task 2500"]
        self.cmb_data_collection = Combobox(root, width=10, height=30)
        self.cmb_data_collection["values"] = self.number_task
        self.cmb_data_collection.set("Workflows")
        self.cmb_data_collection.grid(column=1, row=5)
        self.cmb_data_collection.place(x=250, y=50)
        self.cmb_data_collection.configure(state='readonly')

        self.btn_data_collection = Button(root, text="Select", bg="#1E90FF", fg="#fff", font=self.text_font1, width=7, command=self.data_collection)
        self.btn_data_collection.place(x=340, y=50)

        self.label_infrastructure_monitoring = LabelFrame(root, text="Infrastructure Monitoring", bg="#79CDCD", fg="#8B5A2B", font=self.frame_font)
        self.label_infrastructure_monitoring.place(x=420, y=30, width=150, height=50)
        self.btn_infrastructure_monitoring = Button(root, text="Proceed", bg="#1E90FF", fg="#fff", font=self.text_font1, width=15, command=self.infrastructure_monitoring)
        self.btn_infrastructure_monitoring.place(x=430, y=50)

        self.label_data_demand_forecast = LabelFrame(root, text="Data Demand Forecasting", bg="#79CDCD", fg="#8B5A2B", font=self.frame_font)
        self.label_data_demand_forecast.place(x=580, y=30, width=150, height=50)
        self.btn_data_demand_forecast = Button(root, text="Proceed", bg="#1E90FF", fg="#fff", font=self.text_font1, width=15, command=self.data_demand_forecast)
        self.btn_data_demand_forecast.place(x=590, y=50)

        self.label_data_placement = LabelFrame(root, text="Data Placement", bg="#79CDCD", fg="#8B5A2B", font=self.frame_font)
        self.label_data_placement.place(x=740, y=30, width=150, height=50)
        self.btn_data_placement = Button(root, text="Proceed", bg="#1E90FF", fg="#fff", font=self.text_font1, width=15, command=self.data_placement)
        self.btn_data_placement.place(x=750, y=50)

        self.label_data_object_grouping = LabelFrame(root, text="Data & Object Grouping", bg="#79CDCD", fg="#8B5A2B", font=self.frame_font)
        self.label_data_object_grouping.place(x=900, y=30, width=150, height=50)
        self.btn_data_object_grouping = Button(root, text="Proceed", bg="#1E90FF", fg="#fff", font=self.text_font1, width=15, command=self.data_object_grouping)
        self.btn_data_object_grouping.place(x=910, y=50)



        self.label_replica_placement = LabelFrame(root, text="Replica Placement", bg="#79CDCD", fg="#8B5A2B", font=self.frame_font)
        self.label_replica_placement.place(x=900, y=80, width=150, height=50)
        self.btn_replica_placement = Button(root, text="Proceed", bg="#1E90FF", fg="#fff", font=self.text_font1, width=15, command=self.replica_placement)
        self.btn_replica_placement.place(x=910, y=100)

        self.label_optimal_route_retrieval = LabelFrame(root, text="Optimal Route Retrieval", bg="#79CDCD", fg="#8B5A2B", font=self.frame_font)
        self.label_optimal_route_retrieval.place(x=900, y=130, width=150, height=50)
        self.btn_optimal_route_retrieval = Button(root, text="Proceed", bg="#1E90FF", fg="#fff", font=self.text_font1, width=15, command=self.optimal_route_retrieval)
        self.btn_optimal_route_retrieval.place(x=910, y=150)


        self.label_tables_graph = LabelFrame(root, text="Generate Graphs", bg="#79CDCD", fg="#8B5A2B",
                                             font=self.frame_font)
        self.label_tables_graph.place(x=950, y=480, width=120, height=50)
        self.btn_result_graph = Button(root, text="Proceed", bg="#1E90FF", fg="#fff", font=self.text_font1, width=11,
                                       command=self.tables_graphs)
        self.btn_result_graph.place(x=960, y=500)

        self.btn_clear = Button(root, text="Clear", width=6, command=self.clear)
        self.btn_clear.place(x=950, y=550)
        self.btn_exit = Button(root, text="Exit", width=6, command=self.exit)
        self.btn_exit.place(x=1020, y=550)

        # Horizontal (x) Scroll bar
        self.xscrollbar = Scrollbar(root, orient=HORIZONTAL)
        self.xscrollbar.pack(side=BOTTOM, fill=X)
        # Vertical (y) Scroll Bar
        self.yscrollbar = Scrollbar(root)
        self.yscrollbar.pack(side=RIGHT, fill=Y)

        self.label_output_frame = LabelFrame(root, text="Process Window", bg="#79CDCD", fg="#0000FF", font=self.frame_process_res_font)
        self.label_output_frame.place(x=10, y=80, width=500, height=500)
        # Text Widget
        self.data_textarea_process = Text(root, wrap=WORD, xscrollcommand=self.xscrollbar.set, yscrollcommand=self.yscrollbar.set)
        self.data_textarea_process.pack()
        # Configure the scrollbars
        self.xscrollbar.config(command=self.data_textarea_process.xview)
        self.yscrollbar.config(command=self.data_textarea_process.yview)
        self.data_textarea_process.place(x=20, y=100, width=480, height=470)
        self.data_textarea_process.configure(state="disabled")

        self.label_output_frame = LabelFrame(root, text="Result Window", bg="#79CDCD", fg="#0000FF", font=self.frame_process_res_font)
        self.label_output_frame.place(x=520, y=80, width=370, height=500)
        # Text Widget
        self.data_textarea_result = Text(root, wrap=WORD, xscrollcommand=self.xscrollbar.set, yscrollcommand=self.yscrollbar.set)
        self.data_textarea_result.pack()
        # Configure the scrollbars
        self.xscrollbar.config(command=self.data_textarea_result.xview)
        self.yscrollbar.config(command=self.data_textarea_result.yview)
        self.data_textarea_result.place(x=530, y=100, width=350, height=470)
        self.data_textarea_result.configure(state="disabled")

        if not os.path.exists("..\\Result\\"):
            os.mkdir("..\\Result\\")

        if not os.path.exists("..\\Output\\"):
            os.mkdir("..\\Output\\")

    def edge_fog_initialization(self):
        pass
    def data_collection(self):
        pass
    def infrastructure_monitoring(self):
        pass
    def data_demand_forecast(self):
        pass
    def data_placement(self):
        pass
    def data_object_grouping(self):
        pass
    def replica_placement(self):
        pass
    def optimal_route_retrieval(self):
        pass

    def tables_graphs(self):
        if not os.path.exists("..\\Result\\"):
            os.makedirs("..\\Result\\")

        messagebox.showinfo("Info Message", "Graphs are generated successfully...")

    def clear(self):
        self.btn_edge_fog_initialization.configure(state="normal")
        self.btn_data_collection.configure(state="normal")
        self.btn_infrastructure_monitoring.configure(state="normal")
        self.btn_data_demand_forecast.configure(state="normal")
        self.btn_data_placement.configure(state="normal")
        self.btn_data_object_grouping.configure(state="normal")
        self.btn_replica_placement.configure(state="normal")
        self.btn_optimal_route_retrieval.configure(state="normal")
        self.data_textarea_process.configure(state="normal")
        self.data_textarea_process.delete("1.0", "end")
        self.data_textarea_result.configure(state="normal")
        self.data_textarea_result.delete("1.0", "end")

    def exit(self):
        self.root.destroy()


def generate_hc(text):
    # Encode the text to bytes
    encoded_text = text.encode('utf-8')

    # Create a SHA512 hash object
    hash_object = hashlib.sha512(encoded_text)

    # Return the hexadecimal representation of the hash
    return hash_object.hexdigest()


root = Tk()
root.title("LH-CN and ST-GTN Enabled Energy-Aware Data Placement and Adaptive Caching in Edge–Fog–Cloud Computing")
root.geometry("1100x600")
root.resizable(0, 0)
root.configure(bg="#79CDCD")
od = Main_GUI(root)
root.mainloop()