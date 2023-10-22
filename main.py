import os
    from google.cloud import compute_v1

    def run_django_server(request):
        # This is a very simple example, adapt as necessary
        instance_name = "studybot"
        zone = "us-central1-a"

        ssh_command = (
            "gcloud compute ssh {} --zone={} --command='cd /home/user/django-deploy && python manage.py runserver &'"
            .format(instance_name, zone)
        )
        
        os.system(ssh_command)
        
        return 'Command executed!', 200