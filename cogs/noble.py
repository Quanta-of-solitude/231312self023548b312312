'''
~
witten by Noble#5242(Banned) (using PIL) feel free to edit and make it better.

'''
from __future__ import division
import discord
import operator
import base64
import asyncio
import codecs
import random
import pyimgflip
import time
import datetime
import io
import aiohttp
import urllib.request
import re
import json
import PIL
import os
import shutil
import requests
import urllib.parse
import urbanasync
import glob
import moviepy.editor as mpy
from discord.ext import commands
from bs4 import BeautifulSoup
from sympy import solve
from PIL import Image,ImageFilter,ImageDraw,ImageFont, ImageOps
from discord.ext import commands
from discord.ext import commands
from ext.utility import parse_equation
from ext.colours import ColorNames
from random import randint, choice




class Noble:
    def __init__(self, bot):
        self.bot = bot
        self.stopwatches = {}

    def dostuff(self, text):
        text = str(text)
        text = text.partition("&")[0]
        return text[2:]

    @commands.command()
    async def textgif(self,ctx,*,args):
        '''Turn TEXT to GIF'''
        img = Image.new('RGB', (500, 45),"black")
        d = ImageDraw.Draw(img)
        c = 0
        length = int(len(args))
        font = ImageFont.truetype('Tabitha.ttf', 27)
        for m in range(length):
            x = 9
            d.text((x+c, 5), args[m], fill=(255, 255, 255), font = font)
            img.save('{}.png'.format(m))
            c += 12
        gif_name = 'content'
        fps = 10
        file_list = glob.glob('*.png') # Get all the pngs in the current directory
        list.sort(file_list) # Sort the images by #, this may need to be tweaked for your use case
        clip = mpy.ImageSequenceClip(file_list, fps=fps)
        clip.write_gif('{}.gif'.format(gif_name), fps=fps)
        await ctx.send(file=discord.File('content.gif'))
        await ctx.message.delete()
        for f in glob.glob("*.png"):
            os.remove(f)

    @commands.command()
    async def pil(self, ctx,args, *,member : discord.Member=None):
        '''A SIMPLE DEMO FOR WELCOMING (DEV)'''
        server = ctx.guild
        user = member or ctx.message.author
        avi = user.avatar_url
        url = avi
        response = requests.get(url, stream=True)
        with open('img.png', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        img = Image.open("img.png")
        img.thumbnail((200, 200))
        new_im = Image.new("RGBA", (400,400))
        img.thumbnail((150,150))
        new_im.paste(img,(100,100))
        font = ImageFont.truetype('arial.ttf', 19)
        xoff, yoff = (10,5)
        d = ImageDraw.Draw(new_im)
        d.text((90, 280), args, fill="white",font = font)
        new_im.save("on_test.png")
        await ctx.send(file=discord.File('on_test.png'))
        await ctx.message.delete()

    @commands.command()
    async def pictext(self,ctx,*,args):
        '''Turn Text to PIC'''
        font = ImageFont.truetype('arial.ttf', 21)
        xoff, yoff = (10,5)
        img = Image.new('RGB', (500, 45),'black')
        d = ImageDraw.Draw(img)
        d.text((9, 5), args, fill="white",font = font)
        img.save('content.jpeg')
        await ctx.message.delete()
        await ctx.send(file=discord.File('content.jpeg'))

    @commands.command()
    async def encode(self,ctx,*,args):
        '''Encode ascii Text to base64'''
        decoded_stuff = base64.b64encode('{}'.format(args).encode('ascii'))
        encoded_stuff = str(decoded_stuff)
        encoded_stuff = encoded_stuff[2:len(encoded_stuff)-1]
        await ctx.message.delete()
        await ctx.send(content = "{}".format(encoded_stuff))

    @commands.command()
    async def decode(self,ctx,*,args):
        '''Decode to ascii'''
        strOne = ("%s" % args).encode("ascii")
        pad = len(strOne)%4
        strOne += b"="*pad
        encoded_stuff = codecs.decode(strOne.strip(),'base64')
        decoded_stuff = str(encoded_stuff)
        decoded_stuff = decoded_stuff[2:len(decoded_stuff)-1]
        await ctx.message.delete()
        await ctx.send(content = "{}".format(decoded_stuff))

    @commands.command()
    async def stopwatch(self, ctx):
        """Starts/stops stopwatch"""
        author = ctx.author
        if not author.id in self.stopwatches:
            self.stopwatches[author.id] = int(time.perf_counter())
            await ctx.send(author.mention + " Stopwatch started!")
        else:
            tmp = abs(self.stopwatches[author.id] - int(time.perf_counter()))
            tmp = str(datetime.timedelta(seconds=tmp))
            await ctx.send(author.mention + " Stopwatch stopped! Time: **" + tmp + "**")
            self.stopwatches.pop(author.id, None)

    @commands.command()
    async def memeit(self, ctx, args1,args2):
        'MEME IT! memeit [text1] [text2]'
        api = pyimgflip.Imgflip(username='{}'.format(os.environ.get("memeuser")), password='{}'.format(os.environ.get("memepass")))
        memes = api.get_memes()
        meme = random.choice(memes)
        #print("Generating a meme from template: " + meme.name)
        if args1 == None and args2 == None:
            result = api.caption_image(meme, "I forget to add", "Captions!")
        else:
            result = api.caption_image(meme, "{}".format(args1), "{}".format(args2))
        #print("Meme available at URL: " + result['url'])
        em = discord.Embed()
        em.set_image(url = result['url'])
        try:
            await ctx.send(embed = em)
            await ctx.message.delete()
        except:
            await ctx.send(result['url'])
            await ctx.message.delete()

    @commands.command()
    async def disabled(self,ctx,*, member: discord.Member = None):
        'Make A disabled MEME Image (one pic only) XD'
        server = ctx.guild
        user = member or ctx.message.author
        avi = user.avatar_url
        url = '{}'.format(avi)
        response = requests.get(url, stream=True)
        with open('img2.png', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        img = Image.open("img2.png")
        new_im = Image.open("disability.jpg")
        img.thumbnail((98,98))
        new_im.paste(img,(318,216))
        #new_im.save("disabled.jpg")
        await ctx.message.delete()
        await ctx.send(file=discord.File('disabled.jpg'))


    @commands.command()
    async def kington(self, ctx,*,args):
        'TEXT TO KLINGTON XD'
        URL = "http://mrklingo.freeshell.org/uta/index.php"
        regex = re.compile(r"-{12}\s+(.+?)\s+\-{12}", re.MULTILINE)
        cache = {}

        def translate(phrase):
            try:
                return cache[phrase]
            except KeyError:
                pass

            handle = urllib.request.urlopen(URL, urllib.parse.urlencode({'eng' : phrase, 'language' : 'klingon'}).encode("utf-8"))
            try:
                text = handle.read()
            except:
                return phrase

            match = regex.search(text.decode("utf-8"))
            if not match:
                return phrase

            cache[phrase] = match.group(1)
            return match.group(1)

        word = translate(args)
        await ctx.send(word)
        await ctx.message.delete()

    @commands.command(aliases = ['epicduel', 'epduel'])
    async def epchar(self,ctx, *,args:str = None):
        '''ED  CHAR PAGE'''
        try:
            if args == None:
                await ctx.send("`Error: No Name Provided!`")
                return
            args = args.lower()
            args = args.replace(' ','+')
            url = "{}".format(os.environ.get("ED"))
            url = url+args
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'lxml')
            the_script = []
            script = soup.find_all("script")
            classes ={
            "1": "Bounty Hunter",
            "2": "Mercenary",
            "3": "Tech Mage",
            "4": "Cyber Hunter",
            "5": "Tactical Mercenary",
            "6": "Blood Mage"
            }

            
            for x in script:
                the_script.append(x.text)
            made_script_string = '\n'.join(the_script)
            the_magic = re.compile("'flashvars',(.*?);")
            the_flash_vars = the_magic.findall(made_script_string)
            the_flash_vars = str(the_flash_vars)
            clean_var = the_flash_vars[3:len(the_flash_vars)-4]
            thonk_name = re.compile('charName=(.*)')
            get_name = thonk_name.findall(clean_var)
            get_name = self.dostuff(get_name)


            thonk_class = re.compile('charClassId=(.*)')
            get_class = thonk_class.findall(clean_var)
            get_class = self.dostuff(get_class)
            get_class = classes[get_class]


            thonk_level = re.compile('charLvl=(.*)')
            get_level = thonk_level.findall(clean_var)
            get_level = self.dostuff(get_level)


            thonk_gender = re.compile('charGender=(.*)')
            get_gender = thonk_gender.findall(clean_var)
            get_gender = self.dostuff(get_gender)
            if get_gender == "M":
                get_gender = "Male"
            else:
                get_gender = "Female"


            thonk_1v1 = re.compile('charWins1=(.*)')
            get_1v1 = thonk_1v1.findall(clean_var)
            get_1v1 = self.dostuff(get_1v1)
            get_1v1 = locale.format("%d", int(get_1v1), grouping= True)


            thonk_2v2 = re.compile('charWins2=(.*)')
            get_2v2 = thonk_2v2.findall(clean_var)
            get_2v2 = self.dostuff(get_2v2)
            get_2v2 = locale.format("%d", int(get_2v2), grouping= True)


            thonk_jug = re.compile('charJug=(.*)')
            get_jug = thonk_jug.findall(clean_var)
            get_jug = self.dostuff(get_jug)
            get_jug= locale.format("%d", int(get_jug), grouping= True)


            thonk_fame = re.compile('charLikes=(.*)')
            get_fame = thonk_fame.findall(clean_var)
            get_fame = self.dostuff(get_fame)
            get_fame = locale.format("%d", int(get_fame), grouping= True)


            em = discord.Embed(title = "{}".format(get_name), url = url)
            em.set_thumbnail(url = "https://mmohuts.com/wp-content/uploads/2015/03/EpicDuel_604X423.jpg")
            em.set_author(name = "EpicDuel Character:", icon_url = "https://lh4.googleusercontent.com/-Ol8WkbB2DFo/AAAAAAAAAAI/AAAAAAAAA6M/0UStsojopBo/photo.jpg")
            em.colour = discord.Colour.green()
            em.add_field(name = "Name:", value = get_name,inline = False)
            em.add_field(name = "Gender:", value = get_gender,inline = False)
            em.add_field(name = "Class:", value = get_class,inline = False)
            em.add_field(name = "Level:", value = get_level,inline = False)
            em.add_field(name = "1v1 Wins:", value = get_1v1,inline = False)
            em.add_field(name = "2v2 Wins: ", value = get_2v2,inline = False)
            em.add_field(name = "Jugg Wins:", value = get_jug,inline = False)
            em.add_field(name = "Fame: ", value = get_fame, inline = False)
            await ctx.send(embed = em)
        except Exception as e:
            await ctx.send("`-None Found-`")

    @commands.command(aliases = ['aqchar', 'aqwcharacter'])
    async def aqwchar(self,ctx, *,args:str = None):
        '''AQW  CHAR PAGE'''
        try:
            if args == None:
                await ctx.send("`Error: No Name Provided!`")
                return
            args = args.lower()
            args = args.replace(' ', '+')
            url = "{}".format(os.environ.get("BADGE_AQW"))
            url = url+args
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'lxml')
            the_script = []
            script = soup.find_all("script")

            for x in script:
                the_script.append(x.text)
            made_script_string = '\n'.join(the_script)
            the_magic = re.compile('var flashvars = (.*?);')
            the_flash_vars = the_magic.findall(made_script_string)
            the_flash_vars = str(the_flash_vars)
            clean_var = the_flash_vars[5:len(the_flash_vars)-4]
            #print(clean_var)
            #name
            thonk_name = re.compile('strName=(.*)')
            get_name = thonk_name.findall(clean_var)
            get_name = self.dostuff(get_name)
            #Gender
            thonk_gender = re.compile('strGender=(.*)')
            get_gender = thonk_gender.findall(clean_var)
            get_gender = self.dostuff(get_gender)
            if get_gender == "M":
                get_gender = "Male"
            else:
                get_gender = "Female"
            #LEVEL
            thonk_level = re.compile('intLevel=(.*)')
            get_level = thonk_level.findall(clean_var)
            get_level = self.dostuff(get_level)
            #Class
            thonk_class = re.compile('strClassName=(.*)')
            get_class = thonk_class.findall(clean_var)
            get_class = self.dostuff(get_class)
            #armor
            thonk_ar = re.compile('strArmorName=(.*)')
            get_ar = thonk_ar.findall(clean_var)
            get_ar = self.dostuff(get_ar)
            #Weapon
            thonk_weapon = re.compile('strWeaponName=(.*)')
            get_weapon = thonk_weapon.findall(clean_var)
            get_weapon = self.dostuff(get_weapon)
            #Pet
            thonk_pet = re.compile('strPetName=(.*)')
            get_pet = thonk_pet.findall(clean_var)
            get_pet = self.dostuff(get_pet)
            if not get_pet:
                get_pet = "None"
            badge_info = """__USAGE:__ Use w!aqwbadges "name of the player".\nThe quotations are necessary.\nIf excess of badges, use w!badge "name" "amount" < This will display only the required amount of Badges."""
            em = discord.Embed(title = "{}".format(get_name), url = url)
            em.set_thumbnail(url = "https://www.aq.com/img/network/logo-md-aqw.png")
            em.set_author(name = "AQW Character:", icon_url = "http://aqworldswiki.com/images/aqworldswiki.com/7/77/Artix.png")
            em.colour = discord.Colour.red()
            em.add_field(name = "Name:", value = get_name,inline = False)
            em.add_field(name = "Gender:", value = get_gender,inline = False)
            em.add_field(name = "Level:", value = get_level,inline = False)
            em.add_field(name = "Class Name:", value = get_class,inline = False)
            em.add_field(name = "Armor Name:", value = get_ar,inline = False)
            em.add_field(name = "Weapon Name: ", value = get_weapon,inline = False)
            em.add_field(name = "Pet Name:", value = get_pet,inline = False)
            await ctx.send(embed = em)
        except Exception as e:
            #print(e)
            #
            await ctx.send("`Error: None Found!`")


    @commands.command(aliases=['character','achar'])
    async def aq3dchar(self, ctx, *, args:str = None):
        '''Finding the character page of the player (PC nice)'''
        try:
            player = []
            badges = []
            if args == None:
                await ctx.send(content = "`Missing name`")
                return
            link = "{}".format(os.environ.get("achar"))
            new_text = args.replace(' ','+')
            link = link+new_text
            info = {}
            r = requests.get(link)
            soup = BeautifulSoup(r.content, 'lxml')
            g_data = soup.find_all("h3")
            f_data = soup.find_all("div",{"class": "text-center nopadding"})
            img_data = soup.findAll('img',alt=True,src = True)
            c = soup.find("img", alt=True, src=re.compile(r'\/Content\/img\/char\/.+.png'))

            for n in f_data:
                kjk = n.text
                player.append(kjk)
                lolewii = '\n'.join(player)
            for h in g_data:
                fmf = h.text
                badges.append(fmf)
                klma = '\n'.join(badges)
            info['cl'] = c['alt']

            info['clpic'] = 'https://game.aq3d.com' + c['src']
            #loki = lolewii+"Class:"+"\n"+info['cl']+"\n"+"\n"+" **__Badges__** \n"+" **"+klma+"**"
            player_name = lolewii
            player_class = info['cl']
            player_badges = klma
            #return {"user": loki,"pic": info['clpic']}
            data = f"**Name:** {player_name}\n"
            data += f"**Class:** {player_class}\n\n"
            data += f"**Badges:**\n\n{player_badges}"
            try:
                character_embed = discord.Embed(title = "{}".format(player_name), url = link)
                character_embed.set_author(name = "Character Info:",icon_url = "https://www.aq3d.com/media/1322/aq3d-dragonheadlogo.png" )
                character_embed.add_field(name = "**Class:**", value = player_class, inline = True)
                character_embed.add_field(name = "**__Badges__**", value = player_badges, inline = False)
                character_embed.set_footer(text = "|Char-Page, w!mchar for mobile friendly|",icon_url = self.bot.user.avatar_url)
                character_embed.set_thumbnail(url = "https://image.ibb.co/bTDven/logo_aq3d.png")
                character_embed.set_image(url = "{}".format(info['clpic']))
                character_embed.color=discord.Colour.red()
                await ctx.send(content = "**Character-Page. For title Page use w!titles []**",embed = character_embed)
            except:

                paginated_text = ctx.paginate(data)
                for page in paginated_text:
                    if page == paginated_text[-1]:
                        em = discord.Embed(color= 0000, description = page)
                        em.set_image(url = "{}".format(info['clpic']))
                        em.set_thumbnail(url = "https://image.ibb.co/bTDven/logo_aq3d.png")
                        em.set_footer(text = "|Char-Page, w!mchar for mobile friendly.|",icon_url = self.bot.user.avatar_url)
                        out = await ctx.send(embed = em)
                        break
                    em = discord.Embed(color = 0000, description = page)
                    em.set_image(url = "{}".format(info['clpic']))
                    em.set_thumbnail(url = "https://image.ibb.co/bTDven/logo_aq3d.png")
                    em.set_footer(text = "|Char-Page|",icon_url = self.bot.user.avatar_url)
                    await ctx.send(embed = em)

            del player[:]
            del badges [:]
        except Exception as e:
            await ctx.send("`-None Found-`")



    @commands.command()
    async def dead(self,ctx,*, member: discord.Member = None):
        'Make A dead meme Image (one pic only) XD'
        server = ctx.guild
        user = member or ctx.message.author
        avi = user.avatar_url
        url = '{}'.format(avi)
        response = requests.get(url, stream=True)
        with open('img3.png', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        img = Image.open("img3.png")
        new_im = Image.open("dead.jpg")
        #img.thumbnail((145,190))
        thumb = ImageOps.fit(img, (152,152), Image.ANTIALIAS)
        bimg = ImageOps.expand(thumb, border=10)
        new_im.paste(bimg,(74,12))
        new_im.save("deade.jpg")
        await ctx.message.delete()
        await ctx.send(file=discord.File('deade.jpg'))



def setup(bot):
    bot.add_cog(Noble(bot))
