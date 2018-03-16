import time
import datetime

class Call(object):
    call_id = 1
    def __init__(self, caller_name, phone, reason):
        self.id = Call.call_id
        self.caller_name = caller_name
        self.phone = phone
        self.call_time = datetime.date.today().strftime("%y-%m-%d-%H-%M")
        self.reason = reason
        Call.call_id += 1
    
    def display(self):
        print self.id
        print self.caller_name
        print self.phone
        print self.call_time
        print self.reason
        print "--------"

class CallCenter(object):
    def __init__(self):
        self.calls = []
    
    def add(self, new_call):
        self.calls.append(new_call)
        return self
    
    def remove(self):
        del self.calls[0]
        return self
    
    def print_info(self):
        for call in self.calls:
            call.display()
        return self

    def queue_size(self):
        print "queue size:", str(len(self.calls))

call1 = Call("bob",123456789, "prank")
call2 = Call("fred",1233998, "sickness")
center = CallCenter()
center.add(call1).add(call2).print_info().queue_size()  
center.remove().print_info().queue_size()