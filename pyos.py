import os
import curses
import pycfg
from pyarch import load_binary_into_memory
from pyarch import cpu_t

class task_t:
    def __init__(self):
        self.registrador = [0, 0, 0, 0]
        self.registrador_pc = 0
             
class os_t:
    def __init__(self, cpu, memory, terminal):
        self.cpu = cpu
        self.memory = memory
        self.terminal = terminal
        self.terminal.enable_curses()
        self.console_str = ""
        self.terminal.console_print(
            "this is the console, type the commands here\n")

    def printk(self, msg):
        self.terminal.kernel_print("Atencao!!! " + msg + "\n")

    def panic(self, msg):
        self.terminal.end()
        self.terminal.dprint("Atencao!!! kernel panic: " + msg)
        self.cpu.cpu_alive = False

    def interrupt_keyboard(self):
        key = self.terminal.get_key_buffer()

        if ((key >= ord('a')) and (key <= ord('z'))) or ((key >= ord('A')) and (key <= ord('Z'))) or ((key >= ord('0')) and (key <= ord('9'))) or (key == ord(' ')) or (key == ord('-')) or (key == ord('_')) or (key == ord('.')):
            self.console_str = self.console_str + chr(key)
            self.terminal.console_print("\r" + self.console_str)
        elif key == curses.KEY_BACKSPACE:
            self.console_str = self.console_str[:-1]
            self.terminal.console_print("\r" + self.console_str)
        elif (key == curses.KEY_ENTER) or (key == ord('\n')):
            self.console_comandos()
            self.interpret_cmd(self.console_str)
            self.console_str = ""
            self.terminal.console_print("\r")

    def handle_interrupt(self, interrupt):
        if interrupt == pycfg.INTERRUPT_KEYBOARD:
            self.interrupt_keyboard()
        elif interrupt == pycfg.INTERRUPT_TIMER:
            self.printk("Atencao!!! Tempo nao Implementado!")
        elif interrupt == pycfg.INTERRUPT_MEMORY_PROTECTION_FAULT:
            self.printk("Atencao!!! Sistema esta com falta de memoria")
        return 
    
    
    def interpret_cmd(self, cmd):
        if cmd == "sair":
            self.cpu.cpu_alive = False



    def syscall(self):
        self.printk("Atencao!!! Ainda nao esta implementado o syscall")
        return



    def console_comandos(self):
        comando = self.console_str.split(" ")

        if(self.console_str == "return"):
            if(comando[0] == "return"):
                self.interpret_cmd(self.console_str)
                self.console_str = ""
                self.printk("Exibida Mensagem")
            return