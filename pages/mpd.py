import streamlit as st
import streamlit.components.v1 as components

components.html(
'''
<!-- Bar chart -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/charts.css/dist/charts.min.css">
<style>
    #bar-chart {
        height: 50mm;
        /* max-width: 450mm; */
        background-color: var(--color-bgrd);
        --color-bgrd: rgb(209, 214, 218);
        --color-se-petrol: rgb(0, 154, 154);
        --color-se-purple: rgb(100, 24, 141);
        --color-darkgrey: rgb(33, 33, 33);
        --color-midgrey: rgb(52, 58, 64);
        --color-purpur: rgb(27, 21, 52);
    }
</style>


<!-- Gantt chart -->
<style>
    body,
    html {

        /* background-color: #cddade; */
        /* height: 100%; */
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    }

    .header {
        color: #202125;
        margin-bottom: 40px;
    }

    .header h2 {
        font-weight: 600;
    }

    .header p {
        font-weight: 300;
    }

    .wrapper {
        max-width: var(--custom-wrapper-width);
        /* min-width: 700px; */
        margin: 0 auto;
        /* padding: 40px; */
    }

    .gantt {
        display: grid;
        border: 0;
        border-radius: 12px;
        position: relative;
        overflow: hidden;
        box-sizing: border-box;
        box-shadow: 0 75px 125px -57px #7e8f94;
        border-left: 1px solid rgba(0, 0, 0, 0.534);
        border-right: 1px solid rgba(0, 0, 0, 0.534);
    }

    .gantt__row {
        display: grid;
        grid-template-columns: 150px 1fr;
        background-color: #fff;
    }

    .gantt__row:nth-child(odd) {
        background-color: #f5f5f5;
    }

    .gantt__row:nth-child(odd) .gantt__row-first {
        background-color: #f5f5f5;
    }

    .gantt__row:nth-child(3) .gantt__row-bars {
        border-top: 0;
    }

    .gantt__row:nth-child(3) .gantt__row-first {
        border-top: 0;
    }

    .gantt__row--empty {
        background-color: #ffd6d2 !important;
        z-index: 1;
    }

    .gantt__row--empty .gantt__row-first {
        border-width: 1px 1px 0 0;
    }

    .gantt__row--lines {
        position: absolute;
        height: 100%;
        width: 100%;
        background-color: transparent;
        grid-template-columns: 150px repeat({{ planner_dur[-1] }}, 1fr);
    }

    .gantt__row--lines span {
        display: block;
        border-right: 1px solid rgba(0, 0, 0, 0.1);
    }

    .gantt__row--lines span.marker {
        background-color: rgba(10, 52, 68, 0.13);
        z-index: 2;
    }

    .gantt__row--lines:after {
        grid-row: 1;
        grid-column: 0;
        background-color: #1688b3 45;
        z-index: 2;
        height: 100%;
    }

    .gantt__row--days {
        color: #fff;
        background-color: #0a3444 !important;
        border-bottom: 5px solid rgba(0, 0, 0, 0.1);
        grid-template-columns: 150px repeat({{ planner_dur[-1] }}, 1fr);
    }

    .gantt__row--days .gantt__row-first {
        border-top: 0 !important;
        background-color: #0a3444 !important;
    }

    .gantt__row--bar {
        color: #fff;
        background-color: #464646 !important;
        border-bottom: 1px solid rgba(0, 0, 0, 0.1);
        grid-template-columns: 150px repeat({{ planner_dur[-1] }}, 1fr);
        text-align: center;
        /* padding: 15px 0; */
    }

    .gantt__row--bar .gantt__row-first {
        border-top: 0 !important;
        background-color: #46464694 !important;
        /* padding: 15px 0; */
    }

    .gantt__row--stafftable {
        color: #fff;
        vertical-align: middle;
        text-align: center;
        background-color: #46464694 !important;
        border-top: 5px solid rgba(0, 0, 0, 0.534);
        /* border-bottom: 10px solid rgba(0, 0, 0, 0.1); */
        grid-template-columns: 150px repeat({{ planner_dur[-1] }}, 1fr);
        
        /* padding: 15px 0; */
    }

    .gantt__row--stafftable .gantt__row-first {
        border-top: 0 !important;
        background-color: #46464694 !important;
        border-top: 5px solid rgba(0, 0, 0, 0.534);
        /* padding: 15px 0; */
    }

    .gantt__row--days span {
        text-align: center;
        font-size: 13px;
        align-self: center;
        font-weight: bold;
        padding: 20px 0;
    }

    .gantt__row-first {
        background-color: #fff;
        border-width: 1px 0 0 0;
        border-color: rgba(0, 0, 0, 0.1);
        border-style: solid;
        padding: 15px 0;
        font-size: 13px;
        font-weight: bold;
        text-align: center;
        border-left: 1px solid rgba(0, 0, 0, 0.1);
        /* width: 5cm; */
    }

    .gantt__row-bars {
        list-style: none;
        display: grid;
        /* padding: 9px 0; */
        margin: 0;
        grid-template-columns: repeat({{ planner_dur[-1] }}, 1fr);
        grid-gap: 8px 0;
        border-top: 1px solid rgba(221, 221, 221, 0.8);
        padding: 15px 0;
    }

    .gantt__row-bars li {
        font-weight: 500;
        text-align: left;
        font-size: 14px;
        min-height: 15px;
        background-color: #55de84;
        padding: 5px 12px;
        color: #fff;
        overflow: hidden;
        position: relative;
        cursor: pointer;
        border-radius: 20px;
    }

    .gantt__row-bars li.stripes {
        background-image: repeating-linear-gradient(45deg, transparent, transparent 5px, rgba(255, 255, 255, 0.1) 5px, rgba(255, 255, 255, 0.1) 12px);
    }

    .gantt__row-bars li:before,
    .gantt__row-bars li:after {
        height: 100%;
        top: 0;
        z-index: 4;
        position: absolute;
        background-color: rgba(0, 0, 0, 0.3);
    }

    .gantt__row-bars li:before {
        left: 0;
    }

    .gantt__row-bars li:after {
        right: 0;
    }
</style>


























<!-- MPD -->
<div id="main">
    <section class="preview">
        <!-- printfriendly frame -->
        <table class="no-print" style="margin-left: 4mm;">
            <tr style="height: 4mm;">
                <td style="margin-left: 4mm;"></td>
            </tr>
        </table>

        <div class="print-border">
            <!-- header -->
            <table>
                <tr>
                    <td style="width: 200mm;vertical-align: top"><img class="icon"
                            src="/static/img/Siemens_Energy_logo.png" height=60px></td>
                    <td style="width: 250mm;">Tentative, not binding for execution</td>
                    <td style="width: 50mm;">
                        Project name:
                        <br>
                        Switchgear type:
                        <br>
                        No. of bays:
                        <br>
                        Country / Location:
                    </td>
                    <td style="width: 250mm;">
                        {{ temp_project.project_name }}
                        <br>
                        {{ temp_project.plant_type }}
                        <br>
                        {{ temp_project.number_of_bays }}
                        <br>
                        {{ temp_project.country }}
                    </td>
                    <td style="text-align: right;">
                        {{ date_now }}
                        <br>
                        {{ current_user.department }}
                        <br>
                        {{ current_user.username }}
                        <br>
                        Offer ID: {{ temp_project.project_id }}

                    </td>

                </tr>
            </table>

            <div class="row" style="margin-left: 0mm;height: 5mm;">
            </div>
            <div class="row" style="margin-left: 5mm;">
                <table class="mpd-table">
                        <tr>
                            <td>
                                <!-- gantt chart -->
                                <div class="wrapper">
                                    <div class="gantt">
                                        
                                        <div class="gantt__row gantt__row--days">
                                            <div class="gantt__row-first">Workday</div>
                                            {% for item in planner_dur %}
                                            <span>
                                                {{ item }}
                                            </span>
                                            {% endfor %}
                                        
                                            <div class="gantt__row-first">as date</div>
                                            {% for item in dates_list %}
                                            <span style="background-color:#705914c9;">
                                                {{ item[0] }}
                                                <br>
                                                {{ item[1] }}
                                            </span>
                                            {% endfor %}

                                        </div>

                                        <div class="gantt__row gantt__row--lines">
                                            {% for item in planner_dur %}
                                            <span></span>
                                            {% endfor %}
                                        </div>
                                        <!-- bar chart -->
                                        <div class="gantt__row gantt__row--bar">
                                            <div class="gantt__row-first">
                                                Staff
                                                <table>
                                                    <tr style="height: 4mm;"></tr>
                                                    <tr>
                                                        <td style="width: 2mm;"> </td>
                                                        <td style="width: 6mm;">
                                                            <div id="square-purpur"></div>
                                                        </td>
                                                        <td style="width: 8mm;text-align: left;">local</td>
                                                    </tr>
                                                    <tr>
                                                        <td style="width: 2mm;"> </td>
                                                        <td style="width: 6mm;">
                                                            <div id="square-petrol"></div>
                                                        </td>
                                                        <td style="width: 8mm;text-align: left;">expatriate</td>
                                                    </tr>
                                                </table>
                                            </div>
                                            {% for Day,Resource_Expat,Resource_Local in
                                                zip(planner_bar['Day'],planner_bar['Resource_Expat'],planner_bar['Resource_Local'])
                                                %}
                                            <span>
                                            <!-- chart local-staff -->
                                            <table id="bar-chart"
                                                class="charts-css column show-labels show-primary-axis show-10-secondary-axes">
                                                <tbody>

                                                    <tr>
                                                        <td
                                                            style="--size: calc( {{ Resource_Local }} / 10 ); --color: var(--color-purpur);color: white;">
                                                            {{ Resource_Local }}</td>
                                                            <td
                                                            style="--size: calc( {{ Resource_Expat }} / 10 ); --color: var(--color-se-petrol);color: white;">
                                                            {{ Resource_Expat }}</td>
                                                    </tr>
                                                    
                                                </tbody>
                                            </table>
                                            </span>
                                            {% endfor %}
                                        </div>
                                        <!-- gantt chart itself -->
                                        <div class="gantt__row gantt__row--lines">
                                            {% for item in planner_dur %}
                                            <span></span>
                                            {% endfor %}
                                        </div>

                                        {% for Task,Start,Finish,Workdays in zip(planner_lin['Task'],planner_lin['Start'],planner_lin['Finish'],planner_lin['Workdays']) %}
                                        <div class="gantt__row">
                                            <div class="gantt__row-first">
                                                {{ Task }}
                                            </div>
                                            <ul class="gantt__row-bars">
                                                <li style="grid-column: {{ Start }} / {{ Finish }}; background-color: #7c7c7c; text-align: center">{{ Workdays }} d</li>
                                            </ul>
                                        </div>
                                        {% endfor %}

                                        <!-- staff chart -->
                                        <div class="gantt__row gantt__row--stafftable">
                                            {% for item in staff_list %}
                                                <div class="gantt__row-first">{{ item }}</div>
                                                {% for Noses in planner_staff_noses[item] %}
                                                <span style="margin-top: 3mm;border-bottom: 1px solid rgba(0, 0, 0, 0.534);">{{ Noses }}</span>
                                                {% endfor %}
                                            {% endfor %}
                                        </div>

                                        <!-- test chart -->
                                        <!-- <div class="gantt__row gantt__row--bar">
                                            <div class="gantt__row-first">testtesttestt</div>                                           
                                            <span>
                                            </span>
                                        </div> -->
                                    </div>
                                </div>
                            </td>
                        </tr>
                </table>
            </div>
        </div>
    </section>
</div>






'''
,
    height=600,width=600
)
