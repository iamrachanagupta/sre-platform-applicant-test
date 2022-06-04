from kubernetes import client, config

class utilModels(object):
    def __init__(self):
        self.data = ""

        """
            The function load_incluster_config is used to load the cluster information where clients that expect to be 
            running inside a pod running on kubernetes.
        """
        config.load_incluster_config()

        """
            The function load_kube_config is used to load authentication and cluster information from kube-config file
    and stores them in kubernetes.client.configuration.
        """
        #config.load_kube_config()


        self.v1 = client.CoreV1Api()

    def get_running_pod_count(self, svc_name):
        """
            function to get running pod count based on service name
            :param : service name
        """

        try :
            out = self.v1.list_namespaced_pod(namespace='default', label_selector="service="+svc_name, field_selector="status.phase=Running")
            return len(out.items)
        except :
            print("Something is wrong ")

        return 0

    def get_all_services(self):
        """
            function to get running pods in the cluster in namespace `default` per service
and per application group

        """
        data = []

        #print(self.v1.list_node())
        #print(self.v1.list_namespace())
        output = self.v1.list_namespaced_service(namespace='default')

        for svc in output.items :
            service_info = dict()
            #print("service", svc.metadata.name)
            if svc.metadata.labels and 'applicationGroup' in svc.metadata.labels.keys():
                #print(svc.metadata.labels['applicationGroup'])

                service_info['name'] = svc.metadata.name
                service_info['applicationGroup'] = svc.metadata.labels['applicationGroup']
                service_info['runningPodsCount']=self.get_running_pod_count(service_info['name'])
                data.append(service_info)



        return data

    def get_all_services_by_appGrp(self, app_grp):
        """
            function to get running pods in the cluster in namespace `default` that are part of the same `applicationGroup`
            :param : application group name
        """
        data = []

        output = self.v1.list_namespaced_service(namespace='default', label_selector="applicationGroup="+app_grp)

        for svc in output.items:
            service_info = dict()
            service_info['name'] = svc.metadata.name
            service_info['applicationGroup'] = svc.metadata.labels['applicationGroup']
            service_info['runningPodsCount'] = self.get_running_pod_count(service_info['name'])
            data.append(service_info)


        return data

def  main():
    obj = utilModels()

    print(obj.get_all_services())

if __name__ == "__main__":
    main()
