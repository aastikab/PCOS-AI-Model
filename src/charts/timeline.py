import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
import matplotlib.dates as mdates


def create_timeline():
    """
    Create a timeline chart in the style of Gantt..with labels on the phases
    each project has, as well as tasks with milestone markers. Provide consistency in naming variables so that we can use them later on...the first thing that we are wanting to do is to do the definition of the phases of the project as well as their "corresponding" dates.
    """
    phases = {
        'Phase 1: Initial Development': {
            'start': '2024-03-07',
            'end': '2024-03-21',
            'tasks': [
                'Data preprocessing',
                'Model training',
                'UI development'
            ],
            'color': '#3498db'
        },
        'Phase 2: Core Implementation': {
            'start': '2024-03-22',
            'end': '2024-04-05',
            'tasks': [
                'Data aggregation',
                'Pipeline validation',
                'Frontend dev'
            ],
            'color': '#2ecc71'
        },
        'Phase 3: Integration': {
            'start': '2024-04-06',
            'end': '2024-04-21',
            'tasks': [
                'Clinical partnerships',
                'System testing',
                'Optimization'
            ],
            'color': '#e74c3c'
        }
    }

    """ Create a figure that has two sub-plots for the..milestone timeline + "Gantt" """
    fig, (ax_gantt, ax_milestones) = plt.subplots(
        2,
        1,
        figsize=(15, 10),
        gridspec_kw={'height_ratios': [3, 1]}
    )

    """ Then, do the conversion of the dates of the start & end..in the string
     data format type to the objects that represent date-time as a data structure.. """
    for phase_data in phases.values():
        phase_data['start_date'] = datetime.strptime(
            phase_data['start'], '%Y-%m-%d')
        phase_data['end_date'] = datetime.strptime(
            phase_data['end'], '%Y-%m-%d')

    """ Prepare the chart in the Gantt-esque format. """
    phase_names = list(phases.keys())
    # The goal is to have "one" row per phase
    y_positions = np.arange(len(phase_names))

    for idx, (phase_name, phase_data) in enumerate(phases.items()):
        start_date = phase_data['start_date']
        end_date = phase_data['end_date']

        """ Obviously we want to do the calculation in terms of days for the duration of each phase.. """
        phase_duration = (end_date - start_date).days
        """ Then, we want to draw a horizontal bar for this particular phase. """
        ax_gantt.barh(
            idx,
            width=phase_duration,
            left=start_date,
            color=phase_data['color'],
            alpha=0.8,
            height=0.3
        )
        """ Last but not least place some tasks, along the phase bar! """
        num_tasks = len(phase_data['tasks'])
        for task_idx, task_name in enumerate(phase_data['tasks']):
            """ One important computation is the off-set which means that tasks should be evenly spaced within this very phase.! """
            task_offset_days = (
                phase_duration * (task_idx + 1)) / (num_tasks + 1)
            task_date = start_date + timedelta(days=task_offset_days)
            """ Furthermore, we should add a marker for each task.  """
            ax_gantt.scatter(task_date, idx, color='white',
                             edgecolor='black', zorder=5)
            """ Then, we shoudl "Stagger" the labels of the tasks, stagger them up and down... """
            y_offset = 0.2 if task_idx % 2 == 0 else -0.2
            ax_gantt.annotate(
                task_name,
                (task_date, idx + y_offset),
                xytext=(0, 0),
                textcoords='offset points',
                ha='center',
                va='center',
                fontsize=8,
                bbox=dict(facecolor='white',
                          edgecolor='none', alpha=0.7, pad=1)
            )

    """ In that sense we can style the chart ala Gantt.. """
    ax_gantt.set_yticks(y_positions)
    ax_gantt.set_yticklabels(phase_names)
    ax_gantt.grid(True, alpha=0.3)
    """ Some more formatting; format the date axis for the chart to more cclearly fulfill Gantt's intention! """
    ax_gantt.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax_gantt.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
    plt.setp(ax_gantt.get_xticklabels(), rotation=45)
    """ Here is the preparatory timeline of milestones for our "project progress tracker" which I can only assume is related to our "neural networks" """
    milestones = [
        ('Project Start',  '2024-03-07', '↑\nStart'),
        ('Pipeline Done',  '2024-03-21', '↑\nPipeline'),
        ('Integration',    '2024-04-05', '↑\nCore'),
        ('Completion',     '2024-04-21', '↑\nDelivery')
    ]
    """ Then plot the mile-stones! """
    for _, date_str, label_text in milestones:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        ax_milestones.scatter(date_obj, 0, color='red', zorder=5)
        ax_milestones.annotate(
            label_text,
            (date_obj, 0),
            xytext=(0, 10),
            textcoords='offset points',
            ha='center',
            va='bottom'
        )
    """ Make the connetions..connections with a dashed line """
    milestone_dates = [datetime.strptime(m[1], '%Y-%m-%d') for m in milestones]
    ax_milestones.plot(milestone_dates, [
                       0] * len(milestone_dates), color='gray', linestyle='--')
    """ Style the timelines' milestone """
    ax_milestones.grid(True, alpha=0.3)
    ax_milestones.set_yticks([])
    """ FUrthermore it's important to hide the Y-axis ticks for the time-line! Because then we can, that is "assuming" that the date axis is properly formatted with regard to the milestones!  """
    ax_milestones.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax_milestones.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
    plt.setp(ax_milestones.get_xticklabels(), rotation=45)
    """ Here it is, the main title.. """
    fig.text(0.5, 0.95, 'Project Timeline',
             fontsize=16, ha='center', va='bottom')
    """ The layout should preclude and prevent overlap(s) """
    plt.subplots_adjust(top=0.9, hspace=0.3)
    """ Also, we "can" save the figure without having to click and save it manually. """
    plt.savefig('images/timeline.png', dpi=300,
                bbox_inches='tight', facecolor='white')
    plt.close()


if __name__ == "__main__":
    create_timeline()
