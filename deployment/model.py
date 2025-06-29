import streamlit as st
import pandas as pd
import pickle

def run():
# Load All Files

    with open('model_fix.pkl', 'rb') as file:
        model_fix = pickle.load(file)


    fuel_consumption_rate = st.number_input(label='Input Fuel Consumption Rate',min_value=0.0,max_value=50.00)
    eta_variation_hours = st.number_input(label='Input Estimated Arrival Time Variation (Hours)',min_value=0.0,max_value=24.00)
    traffic_congestion_level = st.number_input(label='Input Traffic Congestion Level',min_value=0.0,max_value=10.00)
    warehouse_inventory_level = st.number_input(label='Input Warehouse Inventory Level',min_value=0.0,max_value=1000.00)
    loading_unloading_time = st.number_input(label='Input Loading And Unloading Time',min_value=0.0,max_value=5.00)
    handling_equipment_availability = st.number_input(label='Input Handling Equipment Availability',min_value=0.0,max_value=1.00)
    order_fulfillment_status = st.number_input(label='Input Order Fulfillment Status',min_value=0.0,max_value=1.00)
    weather_condition_severity = st.number_input(label='Input Weather Condition Severity',min_value=0.0,max_value=1.00)
    port_congestion_level = st.number_input(label='Input Port Congestion Level',min_value=0.0,max_value=10.00)
    shipping_costs = st.number_input(label='Input Shipping Cost (in USD)',min_value=0.0,max_value=100000.00)
    supplier_reliability_score = st.number_input(label='Input Supplier Reliability Score',min_value=0.0,max_value=1.00)
    lead_time_days = st.number_input(label='Input Lead Time (in Days)',min_value=0.0,max_value=20.00)
    historical_demand = st.number_input(label='Input Historical Demand (Unit)',min_value=0.0,max_value=10000.00)
    iot_temperature = st.number_input(label='Input IoT Temperature (In Celcius)',min_value=-100.0,max_value=100.00)
    cargo_condition_status = st.number_input(label='Input Cargo Condition Status',min_value=0.0,max_value=1.00)
    route_risk_level = st.number_input(label='Input Route Risk Level',min_value=0.0,max_value=10.00)
    customs_clearance_time = st.number_input(label='Input Customs Clearance Time',min_value=0.0,max_value=20.00)
    driver_behavior_score = st.number_input(label='Input Driver Behaviour Score',min_value=0.0,max_value=1.00)
    fatigue_monitoring_score = st.number_input(label='Input Fatigue Monitoring Score',min_value=0.0,max_value=1.00)
    month = st.selectbox(label='Month of Shipment (in Number)',options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    year = st.selectbox(label='Year of Shipment',options=[2024, 2025, 2026])

    st.write('In the following is the result of the data you have input : ')
    
    data_inf = pd.DataFrame({
        'fuel_consumption_rate' : fuel_consumption_rate,
        'eta_variation_hours' : eta_variation_hours,
        'traffic_congestion_level' : traffic_congestion_level ,
        'warehouse_inventory_level' : warehouse_inventory_level,
        'loading_unloading_time' : loading_unloading_time,
        'handling_equipment_availability' : handling_equipment_availability,
        'order_fulfillment_status' : order_fulfillment_status,
        'weather_condition_severity' : weather_condition_severity,
        'port_congestion_level' : port_congestion_level,
        'shipping_costs' : shipping_costs,
        'supplier_reliability_score' : supplier_reliability_score,
        'lead_time_days' : lead_time_days,
        'historical_demand' : historical_demand,
        'iot_temperature' : iot_temperature, 
        'cargo_condition_status' : cargo_condition_status,
        'route_risk_level' : route_risk_level,
        'customs_clearance_time' : customs_clearance_time,
        'driver_behavior_score' : driver_behavior_score,
        'fatigue_monitoring_score' : fatigue_monitoring_score,
        'month' : month,
        'year' : year
        }, index=[0])


    if st.button(label='predict'):
    
        # Melakukan prediksi data dummy
        pred_delay_1 = model_fix.predict(data_inf)

        
        st.metric(label="Prediction shipment delay : ", value = pred_delay_1)
