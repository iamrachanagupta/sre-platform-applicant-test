from kubernetes import client, config
import json

class utilModels(object):
    def __init__(self):
        self.data = ""
        #config.load_incluster_config()
        config.load_kube_config()
        self.v1 = client.CoreV1Api()

    def get_running_pod_count(self, svc_name):
        #count = 0
        try :
            #print(svc_name)
            out = self.v1.list_namespaced_pod(namespace='default', label_selector="service="+svc_name, field_selector="status.phase=Running")
            #print(len(out.items))
            return len(out.items)
        except :
            print("Something is wrong ")

        return 0

    def get_all_services(self):

        data = []

        #print(self.v1.list_node())
        #print(self.v1.list_namespace())
        output = self.v1.list_namespaced_service(namespace='default')
        #print(self.v1.list_namespaced_pod(namespace='default'))
        for svc in output.items :
            service_info = dict()
            #print("service", svc.metadata.name)
            if svc.metadata.labels and 'applicationGroup' in svc.metadata.labels.keys():
                #print(svc.metadata.labels['applicationGroup'])

                service_info['name'] = svc.metadata.name
                service_info['applicationGroup'] = svc.metadata.labels['applicationGroup']

                service_info['runningPodsCount']=self.get_running_pod_count(service_info['name'])
                data.append(service_info)

        #return json.dumps(data, indent=4)
        return data



def  main():
    obj = utilModels()

    print(obj.get_all_services())

if __name__ == "__main__":
    main()
