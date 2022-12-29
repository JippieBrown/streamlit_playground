import streamlit as st
import streamlit.components.v1 as components

HtmlFile = open('html/gantt_css.html', 'r', encoding='utf-8')

components.html(
'''

''' + 
str(
    HtmlFile.read()
) + 
'''

























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
