## ----------------------------------------------------##

###  Copyright (c) [2023] [Gabriel-Roewer-Pilger]    ###
###   Version (1.1) Updated in [14.02.2023]          ###

## ----------------------------------------------------##

# Bibliotecas necessárias para execução do código

import tkinter as tk
import sqlite3
import tkinter.messagebox
import os

# Variaveis de entrada

icon = "C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\enova.ico"

# Função que gera a interface do Cadastro de O.S


def cad_os():
    cad_os = tk.Toplevel()
    cad_os.title("Cadastro de O.S")
    cad_os.geometry("800x500")
    cad_os.config(bg='#202020')
    cad_os.iconbitmap(default=icon)

    # Função para conferir o último Código da O.S no banco de dados e definir o próximo código

    def get_last_code():
        with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
            c = conn.cursor()

            c.execute("SELECT COD_OS FROM tb_OS ORDER BY COD_OS DESC LIMIT 1")
            last_code = c.fetchone()
            if last_code is not None:
                last_code = last_code[0]
            else:
                last_code = 0
            new_code = int(last_code) + 1
            return new_code

    # Função para armazenar as informações no banco de dados

    def save_data():
        cod_os = eos1.get()
        desc_os = eos2.get()
        orig_os = eos3.get()
        resp_os = eos4.get()
        tipo_os = eos5.get()
        equip_os = eos6.get()
        setor_os = eos7.get()
        infos_os = eos8.get()

        # Condição que verifica se os campos obrigatórios estão preenchidos

        if eos2.get() == "" or eos3.get() == "" or eos4.get() == "" or eos5.get() == "" or eos6.get() == "" or eos7.get() == "" or eos8.get() == "":
            tkinter.messagebox.showerror(
                "Erro!", "Todos os campos precisam ser preenchidos!")
        else:
            with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
                c = conn.cursor()

                c.execute("INSERT INTO tb_OS (COD_OS, DESC_OS, ORIG_OS, RESP_OS, TIPO_OS, EQUIP_OS, SETOR_OS, INFOS_OS) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                          (cod_os, desc_os, orig_os, resp_os, tipo_os, equip_os, setor_os, infos_os))

                # Parâmetro para limpar os campos após salvar os dados

                conn.commit()
                eos2.delete(0, 'end')
                eos3.delete(0, 'end')
                eos4.delete(0, 'end')
                eos5.delete(0, 'end')
                eos6.delete(0, 'end')
                eos7.delete(0, 'end')
                eos8.delete(0, 'end')
                eos1.delete(0, 'end')
                eos1.insert(0, str(get_last_code()).zfill(3))
                os.system("cls")
                print("Informações inseridas!")

    # Função para fechamento da interface

    def cancelar():
        cad_os.destroy()
        print("Janela fechada")

    # Impressão da interface

    los1 = tk.Label(cad_os, text="Código da O.S")
    los1.grid(row=0, column=0, padx=70, pady=10)

    eos1 = tk.Entry(cad_os, width=40)
    eos1.insert(0, str(get_last_code()).zfill(3))
    eos1.grid(row=0, column=1, padx=10, pady=10)

    los2 = tk.Label(cad_os, text="Descrição da O.S")
    los2.grid(row=1, column=0, padx=10, pady=10)

    eos2 = tk.Entry(cad_os, width=40)
    eos2.grid(row=1, column=1, padx=10, pady=10)

    los3 = tk.Label(cad_os, text="Origem O.S")
    los3.grid(row=2, column=0, padx=10, pady=10)

    eos3 = tk.Entry(cad_os, width=40)
    eos3.grid(row=2, column=1, padx=10, pady=10)

    los4 = tk.Label(cad_os, text="Responsável pela O.S")
    los4.grid(row=3, column=0, padx=10, pady=10)

    eos4 = tk.Entry(cad_os, width=40)
    eos4.grid(row=3, column=1, padx=10, pady=10)

    los5 = tk.Label(cad_os, text="Tipo da O.S")
    los5.grid(row=4, column=0, padx=10, pady=10)

    eos5 = tk.Entry(cad_os, width=40)
    eos5.grid(row=4, column=1, padx=10, pady=10)

    los6 = tk.Label(cad_os, text="Equipamento")
    los6.grid(row=5, column=0, padx=10, pady=10)

    eos6 = tk.Entry(cad_os, width=40)
    eos6.grid(row=5, column=1, padx=10, pady=10)

    los7 = tk.Label(cad_os, text="Setor")
    los7.grid(row=6, column=0, padx=10, pady=10)

    eos7 = tk.Entry(cad_os, width=40)
    eos7.grid(row=6, column=1, padx=10, pady=10)

    los8 = tk.Label(cad_os, text="Informações")
    los8.grid(row=7, column=0, padx=10, pady=10)

    eos8 = tk.Entry(cad_os, width=40)
    eos8.grid(row=7, column=1, padx=10, pady=10)

    save_button = tk.Button(cad_os, text="Gerar O.S", command=save_data)
    save_button.grid(row=9, column=0, columnspan=1, padx=10, pady=10)

    cancel_button = tk.Button(cad_os, text="Cancelar", command=cancelar)
    cancel_button.grid(row=9, column=1, columnspan=4, padx=90, pady=10)

    # Função que gera a interface do cadastro de solicitação de serviço


def cad_ss():
    cad_ss = tk.Toplevel()
    cad_ss.title("Cadastro de SS")
    cad_ss.geometry("800x500")
    cad_ss.config(bg='#202020')
    cad_ss.iconbitmap(default=icon)

    # Função para conferir o último Código da O.S no banco de dados e definir o próximo código

    def get_last_code():
        with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
            c = conn.cursor()

            c.execute("SELECT COD_SS FROM tb_SS ORDER BY COD_SS DESC LIMIT 1")
            last_code = c.fetchone()
            if last_code is not None:
                last_code = last_code[0]
            else:
                last_code = 0
            new_code = int(last_code) + 1
            return new_code

    def save_data():
        cod_ss = ess1.get()
        desc_ss = ess2.get()
        setor_ss = ess3.get()
        resp_ss = ess4.get()
        equip_ss = ess5.get()
        infos_ss = ess6.get()

        # Condição que verifica se os campos obrigatórios estão preenchidos

        if ess2.get() == "" or ess3.get() == "" or ess4.get() == "" or ess5.get() == "" or ess6.get() == "":
            tkinter.messagebox.showerror(
                "Erro!", "Todos os campos precisam ser preenchidos!")
        else:
            with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
                c = conn.cursor()

                c.execute("INSERT INTO tb_SS (COD_SS, DESC_SS, RESP_SS, SETOR_SS, EQUIP_SS, INFOS_SS) VALUES (?, ?, ?, ?, ?, ?)",
                          (cod_ss, desc_ss, resp_ss, equip_ss, setor_ss, infos_ss))

                # Parâmetro para limpar os campos após salvar os dados

                conn.commit()
                ess2.delete(0, 'end')
                ess3.delete(0, 'end')
                ess4.delete(0, 'end')
                ess5.delete(0, 'end')
                ess6.delete(0, 'end')
                ess1.delete(0, 'end')
                ess1.insert(0, str(get_last_code()).zfill(3))
                os.system("cls")
                print("Informações inseridas!")

    # Função para fechamento da interface

    def cancelar():
        cad_ss.destroy()
        print("Janela fechada")

    # Impressão da interface

    lss1 = tk.Label(cad_ss, text="Código")
    lss1.grid(row=1, column=0, padx=10, pady=10)

    ess1 = tk.Entry(cad_ss, width=40)
    ess1.insert(0, str(get_last_code()).zfill(3))
    ess1.grid(row=1, column=1, padx=10, pady=10)

    lss2 = tk.Label(cad_ss, text="Descrição")
    lss2.grid(row=2, column=0, padx=10, pady=10)

    ess2 = tk.Entry(cad_ss, width=40)
    ess2.grid(row=2, column=1, padx=10, pady=10)

    lss3 = tk.Label(cad_ss, text="Setor")
    lss3.grid(row=3, column=0, padx=10, pady=10)

    ess3 = tk.Entry(cad_ss, width=40)
    ess3.grid(row=3, column=1, padx=10, pady=10)

    lss4 = tk.Label(cad_ss, text="Responsável")
    lss4.grid(row=4, column=0, padx=10, pady=10)

    ess4 = tk.Entry(cad_ss, width=40)
    ess4.grid(row=4, column=1, padx=10, pady=10)

    lss5 = tk.Label(cad_ss, text="Equipamento")
    lss5.grid(row=5, column=0, padx=10, pady=10)

    ess5 = tk.Entry(cad_ss, width=40)
    ess5.grid(row=5, column=1, padx=10, pady=10)

    lss6 = tk.Label(cad_ss, text="Informações adicionais")
    lss6.grid(row=6, column=0, padx=10, pady=10)

    ess6 = tk.Entry(cad_ss, width=40)
    ess6.grid(row=6, column=1, padx=10, pady=10)

    save_button = tk.Button(cad_ss, text="Gerar S.S", command=save_data)
    save_button.grid(row=9, column=0, columnspan=1, padx=10, pady=10)

    cancel_button = tk.Button(cad_ss, text="Cancelar", command=cancelar)
    cancel_button.grid(row=9, column=1, columnspan=4, padx=90, pady=10)

    # Função que gera a interface do cadastro de peças


def cad_eqp():
    cad_eq = tk.Toplevel()
    cad_eq.title("Cadastro de Equipamentos")
    cad_eq.geometry("800x500")
    cad_eq.config(bg='#202020')
    cad_eq.iconbitmap(default=icon)

    def get_last_code():
        with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
            c = conn.cursor()

            c.execute("SELECT COD_EQP FROM tb_EQP ORDER BY COD_EQP DESC LIMIT 1")
            last_code = c.fetchone()
            if last_code is not None:
                last_code = last_code[0]
            else:
                last_code = 0
            new_code = int(last_code) + 1
            return new_code

    def save_data():
        cod_eqp = eeqp1.get()
        desc_eqp = eeqp2.get()
        setor_eqp = eeqp3.get()

        # Condição que verifica se os campos obrigatórios estão preenchidos

        if eeqp2.get() == "" or eeqp3.get() == "":
            tkinter.messagebox.showerror(
                "Erro!", "Todos os campos precisam ser preenchidos!")
        else:
            with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
                c = conn.cursor()

                c.execute("INSERT INTO tb_EQP (COD_EQP, DESC_EQP, SETOR_EQP) VALUES (?, ?, ?)",
                          (cod_eqp, desc_eqp, setor_eqp))

                # Parâmetro para limpar os campos após salvar os dados

                conn.commit()
                eeqp2.delete(0, 'end')
                eeqp3.delete(0, 'end')
                eeqp1.delete(0, 'end')
                eeqp1.insert(0, str(get_last_code()).zfill(3))
                os.system("cls")
                print("Informações inseridas!")

    # Função para fechamento da interface

    def cancelar():
        cad_eq.destroy()
        print("Janela fechada")

    # Impressão da interface

    leqp1 = tk.Label(cad_eq, text="Código")
    leqp1.grid(row=1, column=0, padx=10, pady=10)

    eeqp1 = tk.Entry(cad_eq, width=40)
    eeqp1.insert(0, str(get_last_code()).zfill(3))
    eeqp1.grid(row=1, column=1, padx=10, pady=10)

    leqp2 = tk.Label(cad_eq, text="Descrição")
    leqp2.grid(row=2, column=0, padx=10, pady=10)

    eeqp2 = tk.Entry(cad_eq, width=40)
    eeqp2.grid(row=2, column=1, padx=10, pady=10)

    leqp3 = tk.Label(cad_eq, text="Setor")
    leqp3.grid(row=3, column=0, padx=10, pady=10)

    eeqp3 = tk.Entry(cad_eq, width=40)
    eeqp3.grid(row=3, column=1, padx=10, pady=10)

    save_button = tk.Button(cad_eq, text="Gerar S.S", command=save_data)
    save_button.grid(row=4, column=0, columnspan=1, padx=10, pady=10)

    cancel_button = tk.Button(cad_eq, text="Cancelar", command=cancelar)
    cancel_button.grid(row=4, column=1, columnspan=4, padx=90, pady=10)

    # Função para gerar a interface do Menu

    # Função que gera a interface do cadastro de peças


def cad_pcs():
    cad_pc = tk.Toplevel()
    cad_pc.title("Cadastro de Peças")
    cad_pc.geometry("800x500")
    cad_pc.config(bg='#202020')
    cad_pc.iconbitmap(default=icon)

    def get_last_code():
        with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
            c = conn.cursor()

            c.execute("SELECT COD_PCS FROM tb_PCS ORDER BY COD_PCS DESC LIMIT 1")
            last_code = c.fetchone()
            if last_code is not None:
                last_code = last_code[0]
            else:
                last_code = 0
            new_code = int(last_code) + 1
            return new_code

    def save_data():
        cod_pc = epc1.get()
        desc_pc = epc2.get()
        prec_pc = epc3.get()
        est_pc = epc4.get()
        infos_pc = epc5.get()

        # Condição que verifica se os campos obrigatórios estão preenchidos

        if epc2.get() == "" or epc3.get() == "" or epc4.get() == "" or epc5.get() == "":
            tkinter.messagebox.showerror(
                "Erro!", "Todos os campos precisam ser preenchidos!")
        else:
            with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
                c = conn.cursor()

                c.execute("INSERT INTO tb_PCS (COD_PCS, DESC_PCS, PREC_PCS, EST_PCS, INFOS_PCS) VALUES (?, ?, ?, ?, ?)",
                          (cod_pc, desc_pc, prec_pc, est_pc, infos_pc))

                # Parâmetro para limpar os campos após salvar os dados

                conn.commit()
                epc2.delete(0, 'end')
                epc3.delete(0, 'end')
                epc4.delete(0, 'end')
                epc5.delete(0, 'end')
                epc1.delete(0, 'end')
                epc1.insert(0, str(get_last_code()).zfill(3))
                os.system("cls")
                print("Informações inseridas!")

    # Função para fechamento da interface

    def cancelar():
        cad_pc.destroy()
        print("Janela fechada")

    # Impressão da interface

    lpc1 = tk.Label(cad_pc, text="Codigo")
    lpc1.grid(row=1, column=0, padx=10, pady=10)

    epc1 = tk.Entry(cad_pc, width=40)
    epc1.insert(0, str(get_last_code()).zfill(3))
    epc1.grid(row=1, column=1, padx=10, pady=10)

    lcp2 = tk.Label(cad_pc, text="Descrição")
    lcp2.grid(row=2, column=0, padx=10, pady=10)

    epc2 = tk.Entry(cad_pc, width=40)
    epc2.grid(row=2, column=1, padx=10, pady=10)

    lpc3 = tk.Label(cad_pc, text="Preço")
    lpc3.grid(row=3, column=0, padx=10, pady=10)

    epc3 = tk.Entry(cad_pc, width=40)
    epc3.grid(row=3, column=1, padx=10, pady=10)

    lpc4 = tk.Label(cad_pc, text="Estoque")
    lpc4.grid(row=4, column=0, padx=10, pady=10)

    epc4 = tk.Entry(cad_pc, width=40)
    epc4.grid(row=4, column=1, padx=10, pady=10)

    lpc5 = tk.Label(cad_pc, text="Informações adicionais")
    lpc5.grid(row=5, column=0, padx=10, pady=10)

    epc5 = tk.Entry(cad_pc, width=40)
    epc5.grid(row=5, column=1, padx=10, pady=10)

    save_button = tk.Button(cad_pc, text="Cadastrar", command=save_data)
    save_button.grid(row=6, column=0, columnspan=1, padx=10, pady=10)

    cancel_button = tk.Button(cad_pc, text="Cancelar", command=cancelar)
    cancel_button.grid(row=6, column=1, columnspan=4, padx=90, pady=10)

    # Função para gerar a interface do Menu

    # Função que gera a interface do cadastro de peças


def cad_fun():
    cad_f = tk.Toplevel()
    cad_f.title("Cadastro de Funcionários")
    cad_f.geometry("800x500")
    cad_f.config(bg='#202020')
    cad_f.iconbitmap(default=icon)

    def get_last_code():
        with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
            c = conn.cursor()

            c.execute("SELECT COD_FUN FROM tb_FUN ORDER BY COD_FUN DESC LIMIT 1")
            last_code = c.fetchone()
            if last_code is not None:
                last_code = last_code[0]
            else:
                last_code = 0
            new_code = int(last_code) + 1
            return new_code

    def save_data():
        cod_fun = efun1.get()
        nome_fun = efun2.get()
        setor_fun = efun3.get()

        # Condição que verifica se os campos obrigatórios estão preenchidos

        if efun2.get() == "" or efun3.get() == "":
            tkinter.messagebox.showerror(
                "Erro!", "Todos os campos precisam ser preenchidos!")
        else:
            with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
                c = conn.cursor()

                c.execute("INSERT INTO tb_FUN (COD_FUN, NOME_FUN, SETOR_FUN) VALUES (?, ?, ?)",
                          (cod_fun, nome_fun, setor_fun))

                # Parâmetro para limpar os campos após salvar os dados

                conn.commit()
                efun2.delete(0, 'end')
                efun3.delete(0, 'end')
                efun1.delete(0, 'end')
                efun1.insert(0, str(get_last_code()).zfill(3))
                os.system("cls")
                print("Informações inseridas!")

    # Função para fechamento da interface

    def cancelar():
        cad_f.destroy()
        print("Janela fechada")

    # Impressão da interface

    lfun1 = tk.Label(cad_f, text="Código do Funcionário")
    lfun1.grid(row=1, column=0, padx=10, pady=10)

    efun1 = tk.Entry(cad_f, width=40)
    efun1.insert(0, str(get_last_code()).zfill(3))
    efun1.grid(row=1, column=1, padx=10, pady=10)

    lfun2 = tk.Label(cad_f, text="Nome do Funcionário")
    lfun2.grid(row=2, column=0, padx=10, pady=10)

    efun2 = tk.Entry(cad_f, width=40)
    efun2.grid(row=2, column=1, padx=10, pady=10)

    lfun3 = tk.Label(cad_f, text="Setor do Funcionário")
    lfun3.grid(row=3, column=0, padx=10, pady=10)

    efun3 = tk.Entry(cad_f, width=40)
    efun3.grid(row=3, column=1, padx=10, pady=10)

    save_button = tk.Button(cad_f, text="Cadastrar", command=save_data)
    save_button.grid(row=4, column=0, columnspan=1, padx=10, pady=10)

    cancel_button = tk.Button(cad_f, text="Cancelar", command=cancelar)
    cancel_button.grid(row=4, column=1, columnspan=4, padx=90, pady=10)

    # Função que gera a interface do cadastro de setores


def cad_set():
    cad_se = tk.Toplevel()
    cad_se.title("Cadastro de Setores")
    cad_se.geometry("800x500")
    cad_se.config(bg='#202020')
    cad_se.iconbitmap(default=icon)

    def get_last_code():
        with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
            c = conn.cursor()

            c.execute("SELECT COD_SET FROM tb_SET ORDER BY COD_SET DESC LIMIT 1")
            last_code = c.fetchone()
            if last_code is not None:
                last_code = last_code[0]
            else:
                last_code = 0
            new_code = int(last_code) + 1
            return new_code

    def save_data():
        cod_set = eset1.get()
        desc_set = eset2.get()

        # Condição que verifica se os campos obrigatórios estão preenchidos

        if eset2.get() == "":
            tkinter.messagebox.showerror(
                "Erro!", "Todos os campos precisam ser preenchidos!")
        else:
            with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
                c = conn.cursor()

                c.execute("INSERT INTO tb_SET (COD_SET, DESC_SET) VALUES (?, ?)",
                          (cod_set, desc_set))

                # Parâmetro para limpar os campos após salvar os dados

                conn.commit()
                eset2.delete(0, 'end')
                eset1.delete(0, 'end')
                eset1.insert(0, str(get_last_code()).zfill(3))
                os.system("cls")
                print("Informações inseridas!")

    # Função para fechamento da interface

    def cancelar():
        cad_se.destroy()
        print("Janela fechada")

    # Impressão da interface

    lset1 = tk.Label(cad_se, text="Código do Setor")
    lset1.grid(row=1, column=0, padx=10, pady=10)

    eset1 = tk.Entry(cad_se, width=40)
    eset1.insert(0, str(get_last_code()).zfill(3))
    eset1.grid(row=1, column=1, padx=10, pady=10)

    lset2 = tk.Label(cad_se, text="Nome do Setor")
    lset2.grid(row=2, column=0, padx=10, pady=10)

    eset2 = tk.Entry(cad_se, width=40)
    eset2.grid(row=2, column=1, padx=10, pady=10)

    save_button = tk.Button(cad_se, text="Cadastrar", command=save_data)
    save_button.grid(row=4, column=0, columnspan=1, padx=10, pady=10)

    cancel_button = tk.Button(cad_se, text="Cancelar", command=cancelar)
    cancel_button.grid(row=4, column=1, columnspan=4, padx=90, pady=10)

    # Função para gerar a interface do Menu principal


def main():
    main_menu = tk.Tk()
    main_menu.title("Menu-Cadastros")
    main_menu.geometry("170x400")
    main_menu.iconbitmap(default=icon)
    main_menu.config(bg='#202020')

    # Botões de acesso ás demais aplicações

    c_os = tk.Button(main_menu, text="Cadastro de O.S", command=cad_os)
    c_os.grid(row=1, column=1, padx=10, pady=10)

    c_ss = tk.Button(main_menu, text="Cadastro de S.S", command=cad_ss)
    c_ss.grid(row=2, column=1, padx=10, pady=10)

    c_eqp = tk.Button(
        main_menu, text="Cadastro de Equipamentos", command=cad_eqp)
    c_eqp.grid(row=3, column=1, padx=10, pady=10)

    c_pcs = tk.Button(main_menu, text="Cadastro de Peças", command=cad_pcs)
    c_pcs.grid(row=4, column=1, padx=10, pady=10)

    c_fun = tk.Button(
        main_menu, text="Cadastro de Funcionários", command=cad_fun)
    c_fun.grid(row=5, column=1, padx=10, pady=10)

    c_set = tk.Button(main_menu, text="Cadastro de Setores", command=cad_set)
    c_set.grid(row=6, column=1, padx=10, pady=10)

    # Função para fechar a interface

    def cancel_menu():
        main_menu.destroy()
        print()

    # Botão para fechar a interface

    c_left = tk.Button(main_menu, text="Sair", command=cancel_menu)
    c_left.grid(row=7, column=1, padx=10, pady=70)

    main_menu.mainloop()


if __name__ == "__main__":
    main()
