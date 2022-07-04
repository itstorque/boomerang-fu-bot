# -*- coding: utf-8 -*-

import os
import os.path


def main():
    # Explicitly start the application that we want
    # to automate - this is just for sake of this
    # example, in other cases it will likely be
    # running already:
    os.system("cmd /c start wordpad")


    # Pause long enough for the application to
    # show its window:
    snooze(2)


    # We need a real or a dummy AUT for the following
    # function, so start one, and make sure to
    # close it again, too.
    # This assume Squish for Qt; remove (if there is
    # a hooked up AUT already), or adjust as needed):
    ctx = startApplication('"%s/examples/qt/addressbook/addressbook"' % os.environ["SQUISH_PREFIX"])

    try:
        # Hook up the application that we want to
        # automate via its window title:
        hook_up_win_aut_by_title("* - WordPad", squish_for_windows_dir="C:/Users/myuser/Squish for Windows 6.7.1")
    finally:
        # Make sure to close the dummy AUT again:
        ctx.detach()


    # To record on the application, execute to the
    # following command and choose...
    #
    #  Run > Record Snippet
    #
    # ...to start snippet recording:
    test.breakpoint()


def init():
    # To avoid having multiple instances of the AUT
    # running, let's kill it, and start a new
    # instance of it later:
    os.system("taskkill /f /im wordpad.exe 2>nul")


def cleanup():
    # Make sure we kill our AUT after test case
    # execution ends normally:
    os.system("taskkill /f /im wordpad.exe 2>nul")


def hook_up_win_aut_by_title(
        window_title,
        squish_for_windows_dir,
        timeout_secs=20,
        output_file_name="%s/../hook_up_win_aut.txt" % os.path.abspath(os.path.join(squishinfo.testCase, ".."))):
    """
    A hooked up AUT is required for this function to work.
    """

    test.startSection(f'Hook up by window title ("{ window_title }")')
    try:
        # An application context of an actual AUT is required:
        if len(applicationContextList()) == 0:
            raise RuntimeError("A hooked up AUT is required for this function to work. Aborting.")

        ctx = currentApplicationContext()


        # Required:
        os.putenv("SQUISH_RUNNERID", ctx.environmentVariable("SQUISH_RUNNERID"))
        os.putenv("SQUISH_PORT", "%s" % ctx.port)
        os.putenv("SQUISH_SERVERADDRESS", ctx.host)


        # Only to suppress error messages,
        # works without:
        os.putenv("SQUISH_RECORD", "0")
        os.putenv("SQUISH_APPID", "-1")


        # Hook up the AUT process via
        # squish_dir\bin\startaut.exe:
        cmd = 'start "startwinaut" /min cmd /c ""%s/bin/startwinaut" --aut-timeout=%s --window-title="%s" >"%s" 2>&1""'
        cmd = cmd % (squish_for_windows_dir, timeout_secs, window_title, output_file_name)
        test.log("Executing: %s" % cmd)
        os.system(cmd)


        # Verify hook up, log error if not:
        try:
            test.log("Waiting for hook up")
            return waitForApplicationLaunch(timeout_secs)
        except:
            test.fatal("hook_up_win_aut(): No new AUT hooked up")
            import codecs
            lines = codecs.open(output_file_name, "r", "utf-8").read().replace("\r\n", "\n").replace("\r", "\n").split("\n")
            lines2 = []
            for l in lines:
                if len(l.strip()) > 0:
                    lines2.append(l.strip())
            if len(lines2) > 0:
                test.fatal("hook_up_win_aut(): Output from: %s:" % output_file_name)
                for l in lines2:
                    if len(l.strip()) > 0:
                        test.fatal("  " + l)
            raise
    finally:
        test.endSection()